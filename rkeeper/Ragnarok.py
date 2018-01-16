from TextDB import TextDB

class Ragnarok:
    def __init__(self, path):
        self.path = path
        self.db = TextDB(self.path)

    def addRecord(self, rec):
        self.db.addRecord(rec)

    def getRecord(self, i=0):
        return self.db.getRecord(i)

    def getResults(self, format=None, deck=None, oppdeck=None, fields=None):
        pass