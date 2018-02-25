from TextDB import TextDB

class Ragnarok:
    def __init__(self, path):
        self.path = path
        self.db = TextDB(self.path)

    def addRecord(self, rec):
        self.db.addRecord(rec)

    def getRecord(self, i=0):
        return self.db.getRecord(i)

    def getResults(self, selectedFormat=None, deck=None, opp_deck=None, time=None):
        return self.db.getResults(selectedFormat=selectedFormat, deck=deck, opp_deck=opp_deck, time=time)
