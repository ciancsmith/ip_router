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
