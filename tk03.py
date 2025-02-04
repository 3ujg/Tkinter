import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        tekst1 = sisestus1.get()  
        tekst2 = sisestus2.get() 
        tekst3 = sisestus3.get() 
        vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}, Kolmas sisestus: {tekst3}")
        vastus.pack()

    # Esimene sisestusväli
    label = tk.Label(aken, text="Chuck Norris", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    label = tk.Label(aken, text="Chuck Norris", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()
   
    # Kolmas sisestusväli
    label = tk.Label(aken, text="Chuck Norris", font=("Arial",16,"bold"), fg="blue").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()

    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Vajuta mind", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()