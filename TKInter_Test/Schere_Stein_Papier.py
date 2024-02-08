import time
import random
import tkinter as tk

root = tk.Tk()

überschrift = tk.Label(root, text="Schere, Stein, Papier", fg="#ffffff", bg="#000000", height=2, width=25, font=("bold", 25))
überschrift.grid(row=0, column=1)

ergebnis = tk.Label(root, text=("Triff Deine Wahl"),  font=("italic", 25))
ergebnis.grid(row=1, column=0, columnspan=3, pady=10)


def game(player_hand):

    bot_hand = random.choice(["Schere", "Stein", "Papier"])
    ergebnis.config(text=("...Schnick..."), bg="white", font=("bold", 25))
    ergebnis.update()
    time.sleep(0.75)
    ergebnis.config(text=("...Schnack..."), bg="white", font=("bold", 25))
    ergebnis.update()
    time.sleep(0.75)
    ergebnis.config(text=("...Schnuck..."), bg="white", font=("bold", 25))
    ergebnis.update()
    time.sleep(0.75)

    if bot_hand == player_hand:
        ergebnis.config(text=("Ich hatte auch "+player_hand +
                        ". Leider unentschieden"), bg="yellow", font=("bold", 25))

    elif player_hand == "Schere" and bot_hand == "Papier":
        ergebnis.config(text=("Ich hatte Papier! Du hast Gewonnen"),
                        bg="green", font=("bold", 25))

    elif player_hand == "Stein" and bot_hand == "Schere":
        ergebnis.config(text=("Ich hatte Schere! Du hast Gewonnen"),
                        bg="green", font=("bold", 25))

    elif player_hand == "Papier" and bot_hand == "Stein":
        ergebnis.config(text=("Ich hatte Stein! Du hast Gewonnen"),
                        bg="green", font=("bold", 25))

    else:
        ergebnis.config(text=("Ich hatte "+bot_hand +
                        ". Du hast verloren"), bg="red", font=("bold", 25))


def schere():
    game("Schere")


def stein():
    game("Stein")


def papier():
    game("Papier")


scherebild = tk.PhotoImage(file="\scherehand.png")
steinbild = tk.PhotoImage(file="\steinhand.png")
papierbild = tk.PhotoImage(file="\papierhand.png")

schere_button = tk.Button(root, image=scherebild,
                          command=schere, bg="black", height=150, width=250)
schere_button.grid(row=2, column=0)
stein_button = tk.Button(root, image=steinbild,
                         command=stein, bg="black", height=150, width=250)
stein_button.grid(row=2, column=1)
papier_button = tk.Button(root, image=papierbild,
                          command=papier, bg="black", height=150, width=250)
papier_button.grid(row=2, column=2)
freifeld = tk.Label(root, height=5)
freifeld.grid(row=3, column=0, columnspan=3)
quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("", 16))
quit_button.grid(row=4, column=1, pady=5)

widgets = [überschrift, schere_button, ergebnis, freifeld, quit_button]

# das doppelte Padding (pady) muss hier von hand addiert werden
height = sum([widget.winfo_reqheight() for widget in [überschrift, schere_button, ergebnis, freifeld, quit_button]])+30
width = sum([widget.winfo_reqwidth() for widget in [schere_button, überschrift, papier_button]])
root.geometry(f"{width}x{height}")

root.mainloop()
