import matplotlib as plt
from analyse import *

df  = read_table('Brasseries du Montana')

# affichage des brasseries par type

plt.figure(1)
X = 
Y = nb_brasseries_par_type(df)
plt.plot(X,Y)
plt.xlabel('Type de brasserie')
plt.ylabel('Nombre')

