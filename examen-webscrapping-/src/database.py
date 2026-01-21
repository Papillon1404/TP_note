import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


class DatabaseManager:
    
    def _init_(self) :
        self.conn = sqlite3.connect("database.db")
        self.cursor = conn.cursor()

    def create_database(self,nom : str ,colonnes : list) :
        
        # on convertie les noms de colonne sous forme d'énumération de str
        noms_colonnes = str(colonnes[0])
        for c in colonnes[1] : # on initialise à 1 pour l'ajout des virgules
            noms_colonnes += ","+str(c)
        
        # on crée le nom et les colonnes de la table
        self.cursor.execute("CREATE TABLE "+nom+"(noms_colonnes)")  

        pass



    def insert_line(self,infos : list) : # on insère les informations d'une ligne sous forme de liste de valeurs
        
        # on convertie les informations sous forme d'énumération de str
        infos = str(infos[0])
        for valeur in infos[1] : # on initialise à 1 pour l'ajout des virgules
            infos += ","+str(valeur)

        self.cursor.execute("""INSERT INTO movie VALUES
        ("""+infos+""")
        """)
        
        pass



db = DatabaseManager("database.db")