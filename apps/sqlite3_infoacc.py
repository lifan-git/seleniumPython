import os
import sqlite3
class SQLInfoAcc():
    def __init__(self, database):
        self.conn = sqlite3.connect('example.db')
