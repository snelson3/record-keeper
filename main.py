import Tkinter as tk

class App:
    def __init__(self, master):
        self.g1 = tk.StringVar()
        self.g2 = tk.StringVar()
        self.g3 = tk.StringVar()

        frame = tk.Frame(master)
        frame.pack()

        self.txt_greeting = tk.Label(frame, text="This is introductory text for the program")
        self.txt_greeting.pack()

        self.txt_format = tk.Label(frame, text="Format")
        self.txt_format.pack()

        self.ent_format = tk.Entry(frame)
        self.ent_format.pack()

        self.txt_deck = tk.Label(frame, text="My Deck")
        self.txt_deck.pack()

        self.ent_deck = tk.Entry(frame)
        self.ent_deck.pack()

        self.txt_opp_deck = tk.Label(frame, text="Opp Deck")
        self.txt_opp_deck.pack()

        self.ent_opp_deck = tk.Entry(frame)
        self.ent_opp_deck.pack()

        self.txt_g1 = tk.Label(frame, text="G1")
        self.txt_g1.pack()

        self.bt_w_g1 = tk.Radiobutton(frame, text='W', indicatoron=0,
                    width=5, padx=5, variable=self.g1, value='win')
        self.bt_w_g1.pack() # anchor=tk.W )

        self.bt_l_g1 = tk.Radiobutton(frame, text='L', indicatoron=0,
                                      width=5, padx=5, variable=self.g1, value='lose')
        self.bt_l_g1.pack()  # anchor=tk.W )

        self.txt_g2 = tk.Label(frame, text="G2")
        self.txt_g2.pack()

        self.bt_w_g2 = tk.Radiobutton(frame, text='W', indicatoron=0,
                      width=5, padx=5, variable=self.g2, value='win')
        self.bt_w_g2.pack()  # anchor=tk.W )

        self.bt_l_g2 = tk.Radiobutton(frame, text='L', indicatoron=0,
                      width=5, padx=5, variable=self.g2, value='lose')
        self.bt_l_g2.pack()  # anchor=tk.W )

        self.txt_g3 = tk.Label(frame, text="G3")
        self.txt_g3.pack()

        self.bt_w_g3 = tk.Radiobutton(frame, text='W', indicatoron=0,
                      width=5, padx=5, variable=self.g3, value='win')
        self.bt_w_g3.pack()  # anchor=tk.W )

        self.bt_l_g3 = tk.Radiobutton(frame, text='L', indicatoron=0,
                                  width=5, padx=5, variable=self.g3, value='lose')
        self.bt_l_g3.pack()  # anchor=tk.W )

        self.txt_notes = tk.Label(frame, text="Match Notes")
        self.txt_notes.pack()

        self.ent_notes = tk.Entry(frame)
        self.ent_notes.pack()

        self.button = tk.Button(frame,
                             text="Save Match", fg="red",
                             command=self.save)
        self.button.pack(side=tk.BOTTOM)

    def save(self):
        print("Saving now")
        print("Game Results", self.g1.get(),self.g2.get(),self.g3.get())
        print("Format", self.ent_format.get())
        print("My Deck", self.ent_deck.get())
        print("Opponents Deck", self.ent_opp_deck.get())
        print("Match Notes", self.ent_notes.get())

root = tk.Tk()

app = App(root)
root.mainloop()