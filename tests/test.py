from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(chaos.get())
        divines.set(f"{value / 150.0:.2f}")
    except ValueError:
        pass

root = Tk()
root.title("Chaos to Divines")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

chaos = StringVar()
chaos_entry = ttk.Entry(mainframe, width=5, textvariable=chaos)
chaos_entry.grid(column=2, row=1, sticky=(W, E))

divines = StringVar()
ttk.Label(mainframe, textvariable=divines).grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Chaos").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Divines").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

chaos_entry.focus()

root.bind("<Return>", calculate)
root.bind("<KP_Enter>", calculate)

        
root.mainloop()