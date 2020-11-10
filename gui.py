# import tkinter module 
from tkinter import * 
from tkinter import Entry
import router

def run():


    widgets = []

    def process_input():
        label = Label(outputs, text='Your Output Will appear here')
        label.grid(row=0, column=0)
        widgets.append(label)
        if r.get() == 1:
            for l in widgets:
                l.destroy()

            ip = e1.get()
            class_type, networks, hosts, firstAddress, lastAddress = ipc.get_class_stat(ip)
            label = Label(outputs, justify='left' ,text='class: {}\nnetworks: {}\nhosts: {}\nfirst address: {}\nlast address: {}'.format(class_type, 
            networks, hosts, firstAddress, lastAddress))
            label.grid(row=0, column=0)
            widgets.append(label)

        if r.get() == 2:
            for l in widgets:
                l.destroy()

            ip = e1.get()
            subnet = e2.get()
            address, nets,v_host, valid_subs, b_addrs, f_addr, l_addr = ipc.get_subnet_stats(ip, subnet)
            label = Label(outputs, justify='left', text="Address: {}\nSubnets: {}\nAddressable Hosts per subnet: {}\nValid Subnets: {}\nBroadcast Addresses: {}\nFirst Addresses: {}\nLast Addresses: {}".format(address, 
            nets,v_host, valid_subs, b_addrs, f_addr, l_addr))
            label.grid(row=0, column=0)
            widgets.append(label)

        if r.get() == 3:
            for l in widgets:
                l.destroy()
        
            supernet_list = e3.get().split(",")
            print(supernet_list)
            supernet, netmask = ipc.get_supernet_stats(supernet_list)
            print(supernet, netmask)
            label = Label(outputs, justify='left' ,text="Address: {}\nNetwork Mask: {}".format(supernet, netmask))
            label.grid(row=0, column=0)
            widgets.append(label)

    # creating main tkinter window/toplevel 
    master = Tk()
    master.minsize(600, 600)
    master.title("Ip Assignment 1")
    master.iconphoto(False, PhotoImage(file='logo.png'))

    master.columnconfigure(0, weight=1)
    master.rowconfigure(1, weight=1)

    #input frame
    inputs = LabelFrame(master, text="Main Menu", padx=5, pady=5)
    inputs.grid(row=0, column=0, padx=10, pady = 10, sticky = E+W+N+S, columnspan=4)
    inputs.rowconfigure(0, weight=1)
    inputs.columnconfigure(0, weight=1)

    #output frame
    outputs = LabelFrame(master, text="Output", padx=5, pady=5)
    outputs.grid(row=1, column=0, padx=10, pady = 10, sticky = E+W+N+S, columnspan=4)
    outputs.rowconfigure(0, weight=1)
    outputs.columnconfigure(0, weight=1)

    #Everything that goes the user inserts goes in the input frame
    l1 = Label(inputs, text = "IP ADDRESS:") 
    l2 = Label(inputs, text = "SUBNET MASK:")
    l3 = Label(inputs, text = "SUPERNET IP'S:")

    l1.grid(row = 0, column = 0, sticky = W, ipady = 2, ipadx = 2) 
    l2.grid(row = 1, column = 0, sticky = W, ipady = 2, ipadx= 2)
    l3.grid(row = 2, column = 0, sticky = W, ipady = 2, ipadx= 2)

    e1 = Entry(inputs, width=30, bd=5) 
    e2 = Entry(inputs, width=30, bd=5)
    e3 = Entry(inputs, width=30, bd=5)

    e1.grid(row = 0, column = 1, pady = 2, sticky=E+W+N+S) 
    e2.grid(row = 1, column = 1, pady = 2, sticky=E+W+N+S)
    e3.grid(row = 2, column = 1, pady = 2, sticky=E+W+N+S)

    e1.insert(0,"e.g: (192.168.10.0)")
    e2.insert(0, "e.g: (255.255.255.192)")
    e3.insert(0, "e.g: 192.168.10.1,192.168.10.2,....")



    r = IntVar()
    c1 = Radiobutton(inputs, text="ip_stats", variable=r, value=1).grid(row = 0, column= 2, padx=2, pady=2, sticky=W)
    c2 = Radiobutton(inputs, text="subnet_stats", variable=r, value=2).grid(row = 1, column = 2, padx=2, pady=2, sticky=W)
    c3 = Radiobutton(inputs, text="supernet_stats", variable=r, value=3).grid(row = 2, column = 2, padx=2, pady=2, sticky=W)
    action = Button(inputs, text="Process",command=process_input).grid(row=3, column=1, sticky="nsew")
    quit = Button(inputs, text="Quit", command=master.quit, background="red", fg="white").grid(row=3, column=2, sticky="nsew", padx=10)


    mainloop()