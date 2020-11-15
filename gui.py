# import tkinter module
from tkinter import *
from tkinter import Entry
import router as rt


def run():
    # init graph and helper types
    g = rt.Graph()
    widgets = []
    ROUTERS = []

    def process_input():
        label = Label(outputs, text='Your Output Will appear here')
        label.grid(row=0, column=0)
        widgets.append(label)

        # create router
        if r.get() == 0:
            for l in widgets:
                l.destroy()

            router = str(e1.get())
            router_obj = rt.Router(router, g)
            ROUTERS.append(router_obj)
            label = Label(outputs, justify='left',
                          text='Successfully added router with name {}'.format(router_obj.name))
            label.grid(row=0, column=0)
            widgets.append(label)

        # create edge
        if r.get() == 1:
            for l in widgets:
                l.destroy()

            router_a = str(e1.get())
            router_b = str(e2.get())
            cost = int(e3.get())
            g.add_router(router_a, router_b, cost)
            label = Label(outputs, justify='left',
                          text="added connection between {} <--> {} with cost {}".format(router_a, router_b, cost))
            label.grid(row=0, column=0)
            widgets.append(label)

        # get path
        if r.get() == 2:
            for l in widgets:
                l.destroy()

            start = str(e1.get())
            dst = str(e2.get())
            if start in [router.name for router in ROUTERS]:
                for router in ROUTERS:
                    if router.name == start:
                        start = router

                start, finish, path, cost = router.get_path(dst)
                label = Label(outputs, justify="left", text="start: {}\nFinish: {}\nPath: {}\nCost: {}".format(
                    start, finish, "-->".join(path), cost))

            else:
                label = Label(outputs, justify='left',
                              text="Router object for {} does not exist create one and try again".format(start))

            label.grid(row=0, column=0)
            widgets.append(label)

        # delete router
        if r.get() == 3:
            for l in widgets:
                l.destroy()
            router_a = str(e1.get())
            if router_a in g.router_list:
                g.remove_router(router_a)
                label = Label(outputs, justify='left',
                              text="deleted router {}".format(router_a))
            else:
                label = Label(
                    outputs, justify="left", text="No router with identity {} found!".format(router_a))

            label.grid(row=0, column=0)
            widgets.append(label)

        # routing table
        if r.get() == 4:
            for l in widgets:
                l.destroy()

            start = str(e1.get())
            if start in [router.name for router in ROUTERS]:
                print("True")
                t = Text(outputs, height=(len(g.router_list) - 1),
                         width=50, bg="lightgrey")
                t.grid(row=0, column=0, sticky="nsew")

                for router in ROUTERS:
                    if router.name == start:
                        start = router

                path, cost, info = router.print_routing_table()
                head = "{:<8}{:<8} {:<10} {:<10} {:<10}\n".format(
                    "pos", "from", "to", "cost", "path")
                t.insert(END, head)
                row_i = 1
                col_i = 0
                for k, v in info.items():
                    From, to, cost, path = v
                    t.insert(END, "{:<8}{:<8} {:<10} {:<10} {:<10}\n".format(
                        k, From, to, cost, path))

                widgets.append(t)
                t.config(state=DISABLED)

            else:
                label = Label(outputs, justify='left',
                              text="Router object for {} does not exist create one and try again".format(start))

                label.grid(row=0, column=0)
            widgets.append(label)

    def display_help():
        helpWindow = Toplevel(master)
        helpWindow.title("Help Menu")
        helpWindow.maxsize(800, 800)
        h = Scrollbar(helpWindow, orient='horizontal')
        v = Scrollbar(helpWindow, orient='horizontal')
        t = Text(helpWindow, height=(300),
                 width=300, bg="lightgrey")
        t.grid(row=0, column=0, sticky="nsew")

        # create a router info
        t.insert(END, " Create  Router Command\n")
        t.insert(END, "|------------------------|\n")
        t.insert(
            END, "-The first router entry tab must be filled with a router name.\nIt can be anything except a number\n\n-Example ROUTER: 'A' then you click the create router button then click process\n\n-Your output will be displayed it the output box\n")

        # create a router link
        t.insert(END, "\n Create Router Link Command\n")
        t.insert(END, "|------------------------|\n")
        t.insert(
            END, "\n-To create a link enter a Router name in both router sections.\n\n-Example: Router: 'A' , Router: 'B'\n\n-Enter a cost in the cost bar it has to be an integer e.g '7'\n\n-Once all information has been provided click the create a router link button.\n\n-Then Click the process button and output will be given\n")

        t.insert(END, "\n Delete A Router Command\n")
        t.insert(END, "|------------------------|\n")
        t.insert(END, "\n-To delete a node simply enter the router name in the first router tab.\n\n-Click the delete button and process button it will delete the router if present\n")

        t.insert(END, "\n  Path Command\n")
        t.insert(END, "|------------------------|\n")
        t.insert(END, "\n-Simply enter the start router at the top entry and the destination router in the middle entry.\n\n-press path button and process, it will then display the path taken.\n")

        t.insert(END, "\n Routing Table Command\n")
        t.insert(END, "|------------------------|\n")
        t.insert(END, "\n-Enter the router you want to check all paths for in the first router entry tab.\n\n-Then click routing table button and process\n\n-The table will appear in the output.\n\n-Make sure to run the create router command first for the start router or command won't work")
        t.config(state=DISABLED)

    # creating main tkinter window/toplevel
    master = Tk()
    master.minsize(600, 600)
    master.title("Ip Assignment 2")

    master.columnconfigure(0, weight=1)
    master.rowconfigure(1, weight=1)

    # input frame
    inputs = LabelFrame(master, text="Main Menu", padx=5, pady=5)
    inputs.grid(row=0, column=0, padx=10, pady=10,
                sticky=E+W+N+S, columnspan=4)
    inputs.rowconfigure(0, weight=1)
    inputs.columnconfigure(0, weight=1)

    # output frame
    outputs = LabelFrame(master, text="Output", padx=0, pady=0)
    outputs.grid(row=1, column=0, padx=10, pady=10,
                 sticky=E+W+N+S, columnspan=1)
    outputs.rowconfigure(0, weight=1)
    outputs.columnconfigure(0, weight=1)

    # Everything that goes the user inserts goes in the input frame
    l1 = Label(inputs, text="ROUTER:")
    l2 = Label(inputs, text="ROUTER:")
    l3 = Label(inputs, text="COST:")

    l1.grid(row=0, column=0, sticky=W, ipady=2, ipadx=2)
    l2.grid(row=1, column=0, sticky=W, ipady=2, ipadx=2)
    l3.grid(row=2, column=0, sticky=W, ipady=2, ipadx=2)

    e1 = Entry(inputs, width=30, bd=5)
    e2 = Entry(inputs, width=30, bd=5)
    e3 = Entry(inputs, width=30, bd=5)

    e1.grid(row=0, column=1, pady=2, sticky=E+W+N+S)
    e2.grid(row=1, column=1, pady=2, sticky=E+W+N+S)
    e3.grid(row=2, column=1, pady=2, sticky=E+W+N+S)

    e1.insert(0, "e.g: a, A, Mando")
    e2.insert(0, "e.g: b, B, The Dragon of Tatooine")
    e3.insert(0, "e.g: 7, 8, 9")

    r = IntVar()
    c1 = Radiobutton(inputs, text="create router", variable=r, value=0).grid(
        row=0, column=2, padx=2, pady=2, sticky=W)
    c2 = Radiobutton(inputs, text="create router link", variable=r, value=1).grid(
        row=1, column=2, padx=2, pady=2, sticky=W)
    c3 = Radiobutton(inputs, text="path", variable=r, value=2).grid(
        row=2, column=2, padx=2, pady=2, sticky=W)
    c4 = Radiobutton(inputs, text="delete router", variable=r, value=3).grid(
        row=3, column=2, padx=2, pady=2, sticky=W)
    c5 = Radiobutton(inputs, text="routing table", variable=r, value=4).grid(
        row=4, column=2, padx=2, pady=2, sticky=W)

    process = Button(inputs, text="Process", command=process_input).grid(
        row=5, column=1, sticky="nsew")
    help = Button(inputs, text="Help", command=display_help).grid(
        row=5, column=0, sticky="nsew", padx=10)
    quit = Button(inputs, text="Quit", command=master.quit, background="red",
                  fg="white").grid(row=5, column=2, sticky="nsew", padx=10)

    mainloop()

    if __name__ == "__main__":
        run()
