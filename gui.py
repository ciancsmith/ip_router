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
        if r.get() == 1:
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
        if r.get() == 2:
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
        if r.get() == 3:
            for l in widgets:
                l.destroy()

            start = str(e1.get())
            dst = str(e2.get())
            if start in [router.name for router in ROUTERS]:
                print("True")
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

        # routing table
        if r.get() == 4:
            for l in widgets:
                l.destroy()

            start = str(e1.get())
            if start in [router.name for router in ROUTERS]:
                print("True")
                for router in ROUTERS:
                    if router.name == start:
                        start = router

                path, cost, info = router.print_routing_table()

                label_head = Label(outputs, justify='left', text="{:<8}{:<8} {:<10} {:<10} {:<10}".format(
                    "pos", "from", "to", "cost", "path"))
                label_head.grid(row=0, column=0)
                widgets.append(label_head)
                row_i = 1
                col_i = 0
                for k, v in info.items():
                    From, to, cost, path = v
                    label = Label(outputs, justify="left", text="{:<8}{:<8} {:<10} {:<10} {:<10}".format(
                        k, From, to, cost, path))
                    label.grid(row=0, column=col_i)
                    row_i += 1
                    widget.append(label)

            else:
                label = Label(outputs, justify='left',
                              text="Router object for {} does not exist create one and try again".format(start))

            label.grid(row=0, column=0)
            widgets.append(label)

    def display_help():
        pass

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
    outputs = LabelFrame(master, text="Output", padx=5, pady=5)
    outputs.grid(row=1, column=0, padx=10, pady=10,
                 sticky=E+W+N+S, columnspan=4)
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
    c1 = Radiobutton(inputs, text="create router", variable=r, value=1).grid(
        row=0, column=2, padx=2, pady=2, sticky=W)
    c2 = Radiobutton(inputs, text="create router link", variable=r, value=2).grid(
        row=1, column=2, padx=2, pady=2, sticky=W)
    c3 = Radiobutton(inputs, text="path", variable=r, value=3).grid(
        row=2, column=2, padx=2, pady=2, sticky=W)
    c4 = Radiobutton(inputs, text="routing table", variable=r, value=4).grid(
        row=3, column=2, padx=2, pady=2, sticky=W)

    process = Button(inputs, text="Process", command=process_input).grid(
        row=4, column=1, sticky="nsew")
    help = Button(inputs, text="Help", command=display_help).grid(
        row=4, column=0, sticky="nsew", padx=10)
    quit = Button(inputs, text="Quit", command=master.quit, background="red",
                  fg="white").grid(row=4, column=2, sticky="nsew", padx=10)

    mainloop()

    if __name__ == "__main__":
        run()
