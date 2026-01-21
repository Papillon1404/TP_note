import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


class DatabaseManager:
    
    def _init_(self) :
        self.conn = sqlite3.connect("database.db")
        self.cursor = conn.cursor()

    def deconnexion(self):
        self.conn.close()

    
    #### gestion de table #############################################################################################
    
    def creer_table(self,nom : str ,colonnes : list) :
        
        # on convertie les noms de colonne sous forme d'énumération de str
        noms_colonnes = str(colonnes[0])
        for c in colonnes[1] : # on initialise à 1 pour l'ajout des virgules
            noms_colonnes += ","+str(c)
        
        # on crée le nom et les colonnes de la table
        self.cursor.execute("CREATE TABLE "+nom+"(noms_colonnes)")  

    

    def supprimer_table(self,nom : str ) :  

        self.cursor.execute("")


    def vider_table(self,nom : str)  :
        pass 

    def lister_table(self) :
        pass

    def decrire_table(self, nom : str) :
        pass




    #### insertion de donnée #####################################################################################
    
    def inserer_ligne(self,nom : str, infos : list) : # on insère les informations d'une ligne sous forme de liste de valeurs
        
        # conversion en liste de str
        infos_str = []
        for i in infos :
            infos_str.append(str(i))
        
        # on convertie les informations sous forme d'énumération de str
        list_values = str(infos_str[0])
        
        # on initialise à 1 pour l'ajout des virgules
        for valeur in infos_str[1:] : 

            list_values += ","+str(valeur)

        # execution de la commande SQL
        self.cursor.execute("""INSERT INTO"""+nom+""" VALUES
        ("""+infos+""")
        """)
        
        
    def inserer_donnee(self,nom : str, donnee) :

        self.cursor.execute("""INSERT """)
    



    #### Lecture / Requête ##################################################################################################

    def executer_requete(self,nom : str,sql) :

        self.cursor.execute(sql)


    def select_ligne(self,nom : str) : 
        pass

    def select_tout(self,nom : str) :
        pass

    def supprimer_ligne(self,nom : str) :
        pass

    def selectionner_colonne(self,nom : str, colonne) :
        pass

    def compter_lignes(self, nom : str)  :
        pass





    
db = DatabaseManager("database.db")