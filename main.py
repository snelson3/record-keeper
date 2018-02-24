import Tkinter as tk
from rkeeper.Ragnarok import Ragnarok
import time
from autocomplete import Combobox_Autocomplete as autobox

class App:
    def __init__(self, master, db):
        self.widgets = {}
        self.db = db
        self.g1 = tk.StringVar()
        self.g2 = tk.StringVar()
        self.g3 = tk.StringVar()

        frame = tk.Frame(master)
        frame.pack()

        self.widgets['label_greeting'] = tk.Label(frame, text="This is a program to keep track of MTGA records")
        self.widgets['label_greeting'].pack()

        last = self.db.getRecord()
        last_format = ''
        last_deck = ''
        if last:
            if 'format' in last:
                last_format = last['format']
            if 'deck' in last:
                last_deck = last['deck']

        self.drawInput(frame, 'format', 'Format', prevalue=last_format)
        self.drawInput(frame, 'deck', 'My Deck', prevalue=last_deck)
        self.drawInput(frame, 'opp_deck', 'Opp Deck')
        self.drawGameRadioButton(frame, 'g1', 'G1', self.g1) #anchor=tk.W
        self.drawGameRadioButton(frame, 'g2', 'G2', self.g2) #anchor=tk.W
        self.drawGameRadioButton(frame, 'g3', 'G3', self.g3) #anchor=tk.W
        self.drawInput(frame, 'notes', 'Match Notes')
        self.drawButton(frame, 'save', 'Save Match', self.save, tk.BOTTOM)

    def drawGameRadioButton(self, frame, name, title, variable, anchor=None):
        label_name = 'label_' + name
        self.widgets[label_name] = tk.Label(frame, text=title)
        self.widgets[label_name].pack()

        self.widgets['w_' + name] = tk.Radiobutton(frame, text='W', value='win', variable=variable,
                                                   indicatoron=0, width=5, padx=5)
        self.widgets['l_' + name] = tk.Radiobutton(frame, text='L', value='lose', variable=variable,
                                                   indicatoron=0, width=5, padx=5)

        self.widgets['w_' + name].pack(anchor=anchor)
        self.widgets['l_' + name].pack(anchor=anchor)

    def drawInput(self, frame, name, title, prevalue=None):
        label_name = 'label_' + name
        self.widgets[label_name] = tk.Label(frame, text=title)
        self.widgets[label_name].pack()

        self.widgets[name] = tk.Entry(frame)
        if prevalue:
            self.widgets[name].insert(0, prevalue)
        self.widgets[name].pack()

    def drawButton(self, frame, name, text, command, side=None):
        self.widgets[name] = tk.Button(frame, text=text, fg="red", command=command)
        self.widgets[name].pack(side=side)

    def save(self):
        if not self.shouldSave():
            print "Not Saving"
            return
        record = {
            "g1": self.g1.get(),
            "g2": self.g2.get(),
            "g3": self.g3.get(),
            "format": self.widgets['format'].get(),
            "deck": self.widgets['deck'].get(),
            "opp_deck": self.widgets['opp_deck'].get(),
            "notes": self.widgets['notes'].get(),
            "time": time.time()
        }
        print("Saving now")
        print("Game Results", record['g1'], record['g2'], record['g3'])
        print("Format", record['format'])
        print("My Deck", record['deck'])
        print("Opponents Deck", record['opp_deck'])
        print("Match Notes", record['notes'])
        self.db.addRecord(record)
        self.widgets['opp_deck'].delete(0,tk.END)
        self.widgets['notes'].delete(0,tk.END)
        self.g1.set('')
        self.widgets['w_g1'].deselect()
        self.widgets['l_g1'].deselect()
        self.g2.set('')
        self.widgets['w_g2'].deselect()
        self.widgets['l_g2'].deselect()
        self.g3.set('')
        self.widgets['w_g3'].deselect()
        self.widgets['l_g3'].deselect()

        self.widgets['save'].disabled = tk.FALSE

    def shouldSave(self):
        print self.g1.get()
        if len(self.g1.get()) == 0:
            return False
        if len(self.widgets['format'].get()) == 0:
            return False
        if len(self.widgets['deck'].get()) == 0:
            return False
        return True

db = Ragnarok('records.db')
root = tk.Tk()
app = App(root, db)
root.mainloop()