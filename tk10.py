import ttkbootstrap as ttk
from ttkbootstrap.constants import *

aken = ttk.Window(themename="darkly")
aken.geometry("400x400")

def show_selection():
    print("Nupp on vajutatud!")

btn_show = ttk.Button(aken, text="Näita valikut", command=show_selection, bootstyle="warning")
btn_show.pack(pady=20)
label = ttk.Label(aken, text="Sisesta midagi", bootstyle="light")
label.pack(pady=20)

entry = ttk.Entry(aken, bootstyle="info")
entry.pack(pady=20)

checkbox = ttk.Checkbutton(aken, text="Valik 1", bootstyle="success")
checkbox.pack(pady=10)

radiobutton = ttk.Radiobutton(aken, text="Valik 1", bootstyle="danger")
radiobutton.pack(pady=10)

aken.mainloop()