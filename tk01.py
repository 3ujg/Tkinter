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

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

# Peafunktsioon, mis loob Tkinteri akna ja lisab sinna sildi ja nupu
def main():
    aken = tk.Tk()
    aken.title("Mario ülesanded")
    aken.geometry("400x300")
    aken.resizable(True, False)
   # silt
    label = tk.Label(aken, text="Chuck Norris", font=("Arial",16,"bold"), fg="blue").pack()
   # pilt
    kuva_pilt(aken, "chekes.jpg", 200, 200)
   # tekst
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Helvetica", 12, "bold"), fg="blue")
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("text.txt")
    tekst.insert(tk.INSERT, failisisu)
    aken.mainloop()
# Käivitame peafunktsiooni
if __name__ == "__main__":
    main()