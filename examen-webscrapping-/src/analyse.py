import pandas as pd
from database import DatabaseManager as dm

# on suppose qu'on va directement chercher dans database.db donc pas de précision de chemin
def read_table(nom_table : str, colonnes) : 
    data = dm.select_tout(nom_table)
    df = pd.read_csv(data,column = colonnes)

    return df


def nb_brasseries_par_type(df):

    data = df.pd.groupby('Type')['Nom','Type']
    data['nombre par type'] = data.pd.count
    
    return data
