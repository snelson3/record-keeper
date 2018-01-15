import os, shutil
from rkeeper.TextDB import TextDB
from unittest import TestCase

TEST_PATH = "TextDB-tests"
TEST_TXT = os.path.join(TEST_PATH, "test.txt")

class TestTextDB(TestCase):
    def _mkScratchDir(self):
        if (os.path.isdir(TEST_PATH)):
            shutil.rmtree(TEST_PATH, ignore_errors=True)
        os.mkdir(TEST_PATH)

    def test_load_new(self):
        # create a new file
        self._mkScratchDir()
        db = TextDB(TEST_TXT)
        self.assertTrue(db.records == [])
        self.assertTrue(os.path.isfile(TEST_TXT))

    def test_load_old(self):
        # read an old file with 2 records
        self._mkScratchDir()
        with open(TEST_TXT, "w") as f:
            f.write("\n{}\n{}")
        db = TextDB(TEST_TXT)
        self.assertTrue(len(db.records) == 2)

    def test_load_old_bad(self):
        # read a file that isn't valid json and see an exception is raised
        self._mkScratchDir()
        with open(TEST_TXT, "w") as f:
            f.write("\nnot_json")
        try:
            db = TextDB(TEST_TXT)
            self.assertTrue(False, "Was able to load invalid file")
        except:
            self.assertTrue(True)

    def test_addRecord(self):
        # see that a record can get added to a new db
        self._mkScratchDir()
        db = TextDB(TEST_TXT)
        db.addRecord({})
        self.assertTrue(len(db.records) == 1)

    def test_addRecord_existing(self):
        # see that a record can get added to a old db
        self._mkScratchDir()
        with open(TEST_TXT, "w") as f:
            f.write("\n{}\n{}")
        db = TextDB(TEST_TXT)
        db.addRecord({})
        self.assertTrue(len(db.records) == 3)

    def test_addRecord_bad(self):
        self._mkScratchDir()
        db = TextDB(TEST_TXT)
        try:
            db.addRecord("not_json")
            self.assertTrue(False, "Was able to add non json record")
        except:
            self.assertTrue(True)

    def test_getRecord(self):
        self._mkScratchDir()
        db = TextDB(TEST_TXT)
        db.addRecord({"a": True})
        self.assertDictEqual(db.getRecord(), {"a": True})
        db.addRecord({"b": True})
        self.assertDictEqual(db.getRecord(), {"b": True})
        self.assertDictEqual(db.getRecord(1), {"a": True})
        db.addRecord({"c": True})
        db.addRecord({"d": True})
        self.assertDictEqual(db.getRecord(2), {"b": True})
        self.assertDictEqual(db.getRecord(-1), {"a": True})
        self.assertIsNone(db.getRecord(9001))
