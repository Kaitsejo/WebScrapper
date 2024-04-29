import requests
import bs4
import pandas as pd

res = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
#récupération du code la page html
soup = bs4.BeautifulSoup(res.text,"lxml")
#récupération du rating
ratings_data = soup.select('.Rating')
rating= [rating.getText() for rating in ratings_data]
#récupération du pourcentage
percent_data = soup.select('.CocoaPercent')
percent = [ percent.getText() for percent in percent_data]
#fusion des 2 listes en 1 dictionnaire
dict={'per':percent,'rate':rating}
#création du fichier csv
data_cacao=pd.DataFrame(dict)
data_cacao.to_csv('data_cacao.csv',index=False)