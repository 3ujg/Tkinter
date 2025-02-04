import tkinter as tk
from PIL import Image, ImageTk

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open("chekes.jpg")
    p = 50
    pilt = pilt.resize((200, 200))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

# Peafunktsioon, mis loob Tkinteri akna ja lisab sinna sildi ja nupu
def main():
    aken = tk.Tk()
    aken.title("Mario ülesanded")
    aken.geometry("400x300")
    aken.resizable(True, False)
   
    label = tk.Label(aken, text="Chuck Norris", font=("Arial",16,"bold"), fg="blue").pack()
    kuva_pilt(aken, "chekes.jpg", 200, 200)
    aken.mainloop()

# Käivitame peafunktsiooni
if __name__ == "__main__":
    main()