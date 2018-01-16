import json, os
class TextDB():
    def __init__(self, fn):
        self.fn = fn
        self.records = []
        self._load()

    def _ensureGoodFile(self):
        if not os.path.exists(self.fn):
            print "file({}) doesn't exist, creating new database".format(self.fn)
            with open(self.fn, "w") as f:
                f.write("\n")
        with open(self.fn) as f:
            for line in f:
                if line == "\n":
                    continue
                line = line.strip()
                try:
                    json.loads(line)
                except Exception as err:
                    raise Exception("Could not parse line {}, err: {}".format(line, err))
        return True

    def _load(self):
        if self._ensureGoodFile():
            with open(self.fn) as f:
                for line in f:
                    if line == "\n":
                        continue
                    self.records.append(json.loads(line))

    def _appendToFile(self, s):
        with open(self.fn, "a") as f:
            f.write(s + '\n')

    def addRecord(self, record):
        try:
            s = json.dumps(record)
        except Exception as err:
            print "record {} was not valid json, not adding record: {}".format(record, err)
            return False
        self.records.append(record)
        self._appendToFile(s)
        return True

    def getRecord(self, i=0):
        # Get's the i'th newest record, or None if that index doesn't exist
        if i >= len(self.records):
            return None
        return list(reversed(self.records))[i]

    def getResults(self, format=None, deck=None, opp_deck=None, time=None):
        def f(rec):
            if format:
                if 'format' not in rec or rec['format'] != format:
                    return False
            if deck:
                if 'deck' not in rec or rec['deck'] != deck:
                    return False
            if opp_deck:
                if 'opp_deck' not in rec or rec['opp_deck'] != opp_deck:
                    return False
            if time:
                if 'time' not in rec or float(rec['time']) < time:
                    return False
            return True
        return filter(f, self.records)