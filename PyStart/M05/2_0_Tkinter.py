import tkinter as tk
from tkinter import messagebox


def send_name():
    print(first_name.get())
    print("click")
    if first_name.get() == "Seba":
        messagebox.showinfo(title="OK", message="Witam Pana")
    else:
        messagebox.showinfo(title="Nie OK", message="Nie znam")


window = tk.Tk()
window.title("Pystart")

label = tk.Label(window, text="Jak masz na imie?")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()

# pygubu !!! na githubieo nazwie alejandroautalan generowanie xml i go importowanie do pythona
# Tkdocs
