import tkinter as tk
from random import randint

def guess_number():
    diff = abs(target - int(guess.get()))
    if diff == 0:
        tip.configure(text="1 git")
        return
    guesses.append(diff)
    if len(guesses) == 1:
        return

    if guesses[-1] > guesses[-2]:
        # zimno
        tip.configure(text="zimno")
        return
    if guesses[-1] < guesses[-2]:
        # cieplo
        tip.configure(text="cieplo")
        return
    else:
        # git
        tip.configure(text="git")
        return

target = randint(1, 20)
print(target)
guesses = []

window = tk.Tk()
window.geometry("500x500")
window.title("Zgadnij liczbe")

label = tk.Label(window, text="Slucham propozycji")
label.pack()
guess = tk.Entry(window)
guess.pack()

button = tk.Button(window, text="Zgaduje", command=guess_number)
button.pack()

tip = tk.Label(window, text="")
tip.pack()

window.mainloop()
