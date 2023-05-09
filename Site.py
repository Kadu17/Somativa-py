from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Web:
    def __init__(self):
        self.site = 'https://shopee.com.br/'
        self.map = {
            'botao': {
                'xpath': '/html/body/div[1]/div/div[4]/div/div[3]/button[3]'
            },
            'marca': {
                'xpath': '/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div[1]/ul/li[5]/div/a[2]',
                'apple': '/html/body/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div[1]/ul/li[1]/div/div/a'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir()

    def abrir(self):
        sleep(2)
        self.driver.get(self.site)
        sleep(10)
        self.driver.find_element(By.XPATH, self.map['botao']['xpath']).click()
        sleep(5)
        self.driver.find_element(By.XPATH, self.map['marca']['xpath']).click()
        sleep(5)
        self.driver.find_element(By.XPATH, self.map['marca']['apple']).click()
        sleep(5)
        for i in range(1,11):
            print(i, end=' ')




