import sqlite3

class dbconn:
    def __init__(self, file):
        self.file = file
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()
    
    