import requests
import bs4
import pandas as pd
# Etape 1: Utiliser la bibliothèque requests pour lire la page
# Attention, ceci peut ne pas marcher si vous êtes derrière un pare-feu qui bloque Python/Jupyter 
# Il suffit parfois aussi de l'exécuter une deuxième fois pour que cela fonctionne
res = requests.get("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
#récupération du code la page html
soup = bs4.BeautifulSoup(res.text,"lxml")
#récupération de l'entête du tableau
l=0
headers = [th.getText() for th in soup.select('tr')[l].select('th')]
headers.pop(0)
#récupération de des données complète du tableau
rows= soup.select('tr')[3:]
rows_data=[[td.getText() for td in rows[i].findAll('td')]
       for i in range(len(rows))]
#fusion des données en un tableau
data_player = pd.DataFrame(rows_data, columns=headers)
#création du fichier csv
data_player.to_csv('data_player.csv',index=False)