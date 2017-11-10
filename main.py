import Tkinter as tk
import os,json

class Ragnarok:
    def __init__(self, path):
        self.path = path
        self.records = []
        self.load()
    def load(self):
        if not os.path.exists(self.path):
            print "database doesn't exist, can't load"
            return
        with open(self.path) as f:
            self.records = json.load(f)
    def addRecord(self, rec):
        self.records.append(rec)
        self.save()
    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.records,f)
    def getRecord(self,i):
        # Get's the i'th newest record, or None if that index doesn't exist
        if i >= len(self.records):
            return None
        return list(reversed(self.records))[i]

class App:
    def __init__(self, master, db):
        self.db = db
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
        self.ent_format.insert(0,self.db.getRecord(0)['format'])
        self.ent_format.pack()

        self.txt_deck = tk.Label(frame, text="My Deck")
        self.txt_deck.pack()

        self.ent_deck = tk.Entry(frame)
        self.ent_deck.insert(0,self.db.getRecord(0)['deck'])
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
        record = {
            "g1": self.g1.get(),
            "g2": self.g2.get(),
            "g3": self.g3.get(),
            "format": self.ent_format.get(),
            "deck": self.ent_deck.get(),
            "opp_deck": self.ent_opp_deck.get(),
            "notes": self.ent_notes.get()
        }
        print("Saving now")
        print("Game Results", record['g1'], record['g2'], record['g3'])
        print("Format", record['format'])
        print("My Deck", record['deck'])
        print("Opponents Deck", record['opp_deck'])
        print("Match Notes", record['notes'])
        self.db.addRecord(record)
        self.ent_opp_deck.delete(0,tk.END)
        self.ent_notes.delete(0,tk.END)
        self.g1 = tk.StringVar()
        self.g2 = tk.StringVar()
        self.g3 = tk.StringVar()

db = Ragnarok('records.db')
root = tk.Tk()
app = App(root, db)
root.mainloop()