import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("400x100")
    aken.title("Bitch nigga color")
   
    nupp1 = tk.Button(aken, bg="red", fg="white", font=("Arial", 16))
    nupp2 = tk.Button(aken, bg="orange", fg="white", font=("Arial", 16))
    nupp3 = tk.Button(aken, bg="yellow", fg="black", font=("Arial", 16))
    nupp4 = tk.Button(aken, bg="green", fg="white", font=("Arial", 16))
    nupp5 = tk.Button(aken, bg="blue", fg="white", font=("Arial", 16))
    nupp1.pack(side="left", expand=True, fill="x")
    nupp2.pack(side="left", expand=True, fill="x")
    nupp3.pack(side="left", expand=True, fill="x")
    nupp4.pack(side="left", expand=True, fill="x")
    nupp5.pack(side="left", expand=True, fill="x")

    vastus = tk.label(aken, textf"Siia tuleb vastus")
    vastus.pack(side="top", expand=True, fill="x"
    aken.mainloop()

if __name__ == "__main__":
    main()