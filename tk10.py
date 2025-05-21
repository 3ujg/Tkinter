import ttkbootstrap as ttk
from ttkbootstrap.constants import *

aken = ttk.Window(themename="darkly")
aken.geometry("400x400")

def show_selection():
    print("Nupp on vajutatud!")

btn_show = ttk.Button(aken, text="Näita valikut", command=show_selection, bootstyle="warning")
btn_show.pack(pady=20)



aken = ttk.Tk()
aken.title("Raadionuppude näidis")
aken.geometry("300x400")


def show_selection():
    print("Hind:", selected_color.get())
    print(var1.get(), float(var2.get()), var3.get())
    print(selected_option.get())
    if selected_option.get()=="Kuller":
        trans = 3
    else:
        trans = 0
    summa = selected_color.get() + var1.get() + float(var1.get()) + var3.get() + trans
    print(summa)
    
# StringVar, mis hoiab valitud värvi nime
selected_color = tk.IntVar(value=5)



ttk.Label(aken, text="Kasutaja ID", font="Arial,16").pack(pady=(10, 0))
ttk.Entry(aken).pack()



# meetod uue akna avamiseks
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("Uus aken")
    new_window.geometry("200x300")
    ttk.Label(new_window, text="See on uus aken").pack()
    ttk.Button(new_window, text="Sulge aken", command=new_window.destroy).pack()



def show_selection():
    print("Valitud värv:", selected_color.get())

#StringVar, mis hoiab valitud värvi nime
selected_color = ttk.StringVar(value=5)


#Loome raadionupud
ttk.Label(aken, text="Vali pitsa suurus", font="Arial 14").pack()
radio_red = tk.Radiobutton(aken,text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken,text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken,text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = ttk.IntVar(value=0)
var2 = ttk.StringVar(value=0)
var3 = ttk.IntVar(value=0)
ttk.Label(aken, text="Vali lisandid", font="Arial 14").pack()

# Checkbox
checkbox1 = ttk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = ttk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = ttk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()


# dropdown
ttk.Label(aken, text="Vali transport", font="Arial 14").pack()
valikud = ["Kuller", "Kohapeal"]
selected_option = ttk.StringVar()
selected_option.set("Vali üksus")

dropdown = ttk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

btn_confirm = ttk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()


aken.mainloop()