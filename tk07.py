import tkinter as tk

def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        validation_label.config(text="Korras!", fg="green")
    else:
        validation_label.config(text="Isikukood peab olema 11 numbrit", fg="red")

aken = tk.Tk()
aken.title("Validaator")
# Set window size (width x height)
aken.geometry("400x300")

# Add padding to the entire window
aken.configure(padx=20, pady=20)

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

title_label = tk.Label=aken, text="Isikukood:", font="Arial 16", 16, "bold")
title_label.pack(pady=(10, 5))

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Sisesta 11 numbrit!", fg="red")
validation_label.pack()

aken.mainloop()