import tkinter as tk



aken = tk.Tk()
aken.title("Raadionuppude näidis")
aken.geometry("300x400")



def show_selection():
    # print("Hind", selected_color.get())
    # print(var1.get(), float(var2.get()), var3.get())
    # print(selected_option.get())
    if selected_option.get()=="Kuller":
        trans = 3
    else:
        trans = 0
    summa = selected_color.get() + var1.get() + float(var2.get()) + var3.get() + trans
    print(summa)

label = tk.Label(aken, text="Kasutaja ID", font=("Arial",16,"bold"), fg="black").pack()

tk.Label(aken, text="Kasutaja ID", font="Arial 16").pack(pady=(10, 0))
#Tekst
tekst = tk.Text(aken, wrap=tk.WORD, font=("Helvetica", 12, ), fg="black", height=1, width=10)
tekst.pack(expand=False, fill=tk.BOTH)


# meetod uue akna avamiseks
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("Uus aken")
    new_window.geometry("200x300")
    tk.Label(new_window, text="See on uus aken").pack()
    tk.Button(new_window, text="Sulge aken", command=new_window.destroy).pack()



def show_selection():
    print("Valitud värv:", selected_color.get())

#StringVar, mis hoiab valitud värvi nime
selected_color = tk.StringVar(value=5)


#Loome raadionupud
radio_red = tk.Radiobutton(aken,text="Väike (5€)", variable=selected_color, value=0)
radio_green = tk.Radiobutton(aken,text="Suur (8€)", variable=selected_color, value=0)
radio_blue = tk.Radiobutton(aken,text="Pere (12€)", variable=selected_color, value=0)
radio_red.pack()
radio_green.pack()
radio_blue.pack()


var1 = tk.IntVar(value=0)
var2 = tk.StringVar(value=0)
var3 = tk.IntVar(value=0)


# Checkbox
checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

#dropdown
valikud = ["Kuller", "Kohapeal"]
selected_option = 





















aken.mainloop()