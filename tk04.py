import tkinter as tk



def main():

    def kuva_varv(v):
        vastus.config(text=v, font=("Arial", 16), fg=v)
    aken = tk.Tk()

    aken.geometry("400x100")
    aken.title("Bitch nigga color")
   
    nupp1 = tk.Button(aken, bg="red", fg="white", font=("Arial", 16), command=lambda: kuva_varv("red"))
    nupp2 = tk.Button(aken, bg="orange", fg="white", font=("Arial", 16), command=lambda: kuva_varv("orange"))
    nupp3 = tk.Button(aken, bg="yellow", fg="black", font=("Arial", 16), command=lambda: kuva_varv("yellow"))
    nupp4 = tk.Button(aken, bg="green", fg="white", font=("Arial", 16), command=lambda: kuva_varv("green"))
    nupp5 = tk.Button(aken, bg="blue", fg="white", font=("Arial", 16), command=lambda: kuva_varv("blue"))
    vastus = tk.Label(aken, text=f"Siia tuleb vastus")
    vastus.pack(side="bottom", expand=True, fill="x")
    nupp1.pack(side="left", expand=True, fill="x")
    nupp2.pack(side="left", expand=True, fill="x")
    nupp3.pack(side="left", expand=True, fill="x")
    nupp4.pack(side="left", expand=True, fill="x")
    nupp5.pack(side="left", expand=True, fill="x")
    aken.mainloop()

if __name__ == "__main__":
    main()