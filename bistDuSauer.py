import tkinter as tk
import random

class BistDuSauer:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("400x200")
        self.root.title("Bist du sauer?")

        self.label = tk.Label(self.root, text="Bist du sauer?", font=("Montserrat", 18, "bold"))
        self.label.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, text="JA", font=("Montserrat", 18, "bold"), command=self.ja_pressed)
        self.button1.place(x=50, y=100, width=100, height=50)

        self.button2 = tk.Button(self.root, text="NEIN", font=("Montserrat", 18, "bold"), command=self.nein_pressed)
        self.button2.place(x=250, y=100, width=100, height=50)

        self.counter = 0

        self.root.mainloop()

    def ja_pressed(self):
        self.button1.destroy()
        self.button2.destroy()
        text = "Wusste ich es doch,\nsag doch einfach wenn\ndu sauer bist. ☺️"
        label = tk.Label(self.root, text=text, font=("Montserrat", 14), justify=tk.CENTER, wraplength=self.root.winfo_width()-20)
        label.pack(padx=10, pady=10)


    def nein_pressed(self):
        self.counter += 1
        if self.counter == 1:
            x = random.randint(0, self.root.winfo_width() - self.button2.winfo_width())
            y = random.randint(0, self.root.winfo_height() - self.button2.winfo_height())
            self.button2.place(x=x, y=y)
        elif self.counter > 1:
            while True:
                x = random.randint(0, self.root.winfo_width() - self.button2.winfo_width())
                y = random.randint(0, self.root.winfo_height() - self.button2.winfo_height())
                self.button2.place(x=x, y=y)
                self.root.update_idletasks()
                if self.ja_pressed_flag:
                    break

BistDuSauer()
