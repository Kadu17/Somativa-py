import pandas as pd
import requests
from bs4 import BeautifulSoup

listadesc = []
listaprec = []

site = requests.get('https://shopee.com.br/Iphone-col.1214627')
site = BeautifulSoup (site.content, 'html.parser')

nome = site.select("div class")
valor = site.find('div')


for c in valor:
    print(c)
    
    listadesc.append(c)

for c in valor:
    c.text
    listaprec.append(c)

listaprod = {"Descrição": listadesc, "Preço": listaprec}
# plan = pd.DataFrame(listaprod)

# plan.to_excel("Web.xlsx")
