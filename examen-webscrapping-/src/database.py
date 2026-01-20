import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


class DatabaseManager:
    
    def _init_(self) :
        self.conn = sqlite3.connect("database.db")
        self.cursor = conn.cursor()
        

    def insert_brewery(self,name,street,city,state/pronvince,) :
        db.add()
        
        
        
        pass



db = DatabaseManager("database.db")