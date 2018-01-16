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