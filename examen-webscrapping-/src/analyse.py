import pandas as pd
from database import DatabaseManager as dm

# Lecture d'une table SQLite et conversion en DataFrame
def read_table(nom_table: str, colonnes: list):
    data = dm.select_tout(nom_table)  # renvoie une liste de tuples
    df = pd.DataFrame(data, columns=colonnes)
    return df


# Nombre de brasseries par type
def nb_brasseries_par_type(df):
    data = df.groupby('Type').size().reset_index(name='nombre_par_type')
    return data


# Nombre de brasseries par ville
def nb_brasseries_par_ville(df):
    data = df.groupby('Ville').size().reset_index(name='nombre_par_ville')
    return data


# Ville la plus représentée
def ville_plus_representee(df):
    data = nb_brasseries_par_ville(df)
    return data.loc[data['nombre_par_ville'].idxmax()]


# Moyenne du nombre de brasseries par ville
def moyenne_par_ville(df):
    data = nb_brasseries_par_ville(df)
    return data['nombre_par_ville'].mean()


# Proportion d’un type de brasserie dans une ville donnée
def proportion_type_brasserie(df, ville):
    df_ville = df[df['Ville'] == ville]
    total = len(df_ville)

    if total == 0:
        return 0
    else : 
        proportions = df_ville.groupby('Type').size() / total
        return proportions.reset_index(name='proportion')
