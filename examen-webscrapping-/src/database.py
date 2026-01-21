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
        for c in colonnes[1:] : # on initialise à 1 pour l'ajout des virgules
            noms_colonnes += ","+str(c)
        
        # on crée le nom et les colonnes de la table
        self.cursor.execute("CREATE TABLE "+nom+"(noms_colonnes)")  

    

    def supprimer_table(self,nom : str ) :  
        self.cursor.execute("DROP TABLE "+nom)

    def vider_table(self,nom : str)  :
        self.cursor.execute("TRUNCATE TABLE "+nom) 

    def lister_table(self) :
        self.cursor.execute(".tables")

    def decrire_table(self, nom : str) :
        self.cursor.execute(".schema"+nom)




    #### insertion de donnée #####################################################################################
    
    # focntion qui permet d'insérer une liste de donnée sur les colonnes respectivement indiquée par une autre liste
    def inserer_donnees(self,nom : str,id : int ,colonne : list ,infos : list) : # on insère les informations d'une ligne sous forme de liste de valeurs
        
        # conversion en liste de str
        infos_str = []
        for i in infos :
            infos_str.append(str(i))
        
        # on convertie les informations sous forme d'énumération de str
        list_values = str(infos_str[0])
        
        # on initialise à 1 pour l'ajout des virgules
        for valeur in infos_str[1:] : 

            list_values += ","+str(valeur)

        # on fait la meme chose pour les colonnes
        colonnes_str = str(colonne[0])
        for n in colonne[1:] : 
            list_values += ","+str(n)

        if id :
        # execution de la commande SQL avec précision de la ligne
            self.cursor.execute("""INSERT INTO"""+nom+"""("""+colonnes_str+""") SELECT """+int(id)+"""
        ("""+infos+""")
        """)
        
        else :
        # execution de la commande SQL avec précision de la ligne
            self.cursor.execute("""INSERT INTO"""+nom+"""("""+colonnes_str+""") VAMUES 
        ("""+infos+""")
        """)



    #### Lecture / Requête ##################################################################################################

    def executer_requete(self,sql) :
        request = self.cursor.execute(sql)
        request.fetchall()

    def select_ligne(self,nom : str, ligne : str) : 
        request = self.cursor.execute(" SELECT "+ligne+" FROM "+nom)
        request.fetchall()
        
    def select_tout(self,nom : str) :
        request = self.cursor.execute(" SELECT * FROM "+nom)
        request.fetchall()

    def supprimer_ligne(self,nom : str, condition : str) :
        self.cursor.execute(" DELETE FROM "+nom+" WHERE "+condition)
        
    def selectionner_colonnes(self,nom : str, colonnes : list) :
        # on reconvertis en str, l'avantage et d'avoir une utilisation similaire à pandas
        # on garde par ailleurs la possibilité d'afficher les colonnes dans l'ordre que l'on veut
        colonnes_str  =  colonnes[0]
        for c in colonnes[1:] :
            colonnes_str += ','+str(c)

        request = self.cursor.execute(" SELECT "+colonnes_str+" FROM "+nom)
        request.fetchall()

    def compter_lignes(self, nom : str)  :
        # ici on ne rajoute pas de condition, cela n'apporterait aucun gain de temps par rapport a executer_requete(sql)
        request = self.cursor.execute("COUNT(*) FROM "+nom)
        request.fetchall()


