import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  
        kuuintressimäär = float(sisestus2.get())/12 
        maksete_arv = int(sisestus3.get())*12 

        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär)** -maksete_arv)
        
        vastus = tk.Label(aken, text=f"Igakuine makse: {maksete_arv:.2f}")
        vastus.pack()

    # Esimene sisestusväli
    label = tk.Label(aken, text="Laenusumma", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    label = tk.Label(aken, text="Aastane intressimäär (%)", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()
   
    # Kolmas sisestusväli
    label = tk.Label(aken, text="Laenuperiood (Aastates)", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()

    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Vajuta mind", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()