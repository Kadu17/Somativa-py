from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# import Conexao
import pandas as pd

class Web:
    def __init__(self):
        self.site = ['https://shopee.com.br/Iphone-col.1214627','https://shopee.com.br/Samsung-col.1214628','https://shopee.com.br/Motorola-col.1214629','https://shopee.com.br/Xiaomi-col.1214630']
        self.map = {
             'botao': {
                'xpath': '/html/body/div[1]/div/div[4]/div/div[3]/button[3]'
            },
            'marca': {
                'xpath': '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/a/div/div/div[2]/div['
                         '1]/div[1]/div',
                'apple': '/html/body/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div[1]/ul/li[1]/div/div/a',
                'celulares': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[$$]/a/div/div/div['
                             '2]/div[1]/div[1]/div',
                'valores':   '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[$$]/a/div/div/div['
                             '2]/div[2]/div/span[2]'
            },

        }

        for site in self.site:
           self.driver = webdriver.Chrome()
           self.driver.maximize_window()
           self.abrir(site)

    def abrir(self,site):
        self.driver.get(site)
        lista1 = []
        lista2 = []

        sleep(2)
        for i in range(1,11):
            celular = self.map['marca']['celulares'].replace("$$", f"{i}")
            item = self.driver.find_element(By.XPATH, celular).text
            print(item)
            valores = self.map['marca']['valores'].replace("$$", f"{i}")
            item1 = self.driver.find_element(By.XPATH, valores).text
            print(item1)

            # Conexao.inserir(descricao=item, valor=item1)

            lista1.append(item)
            lista2.append(item1)

        descricao = []
        preco = []



        for i in enumerate(lista1):
            print(i)
            descricao.append(i[1])
        for i in enumerate(lista2):
            preco.append("R$"+i[1])
            print(i)

        df = pd.DataFrame({"descricao": descricao, "preco":preco})
        print(df)


        df.to_excel("Web.xlsx")
