from tkinter import ttk, Tk
from tkinter import *

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()

    def tela(self):
        self.janela.title("Web Scrapping")
        self.janela.configure(background="lightBlue")
        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=800)
        self.janela.mainloop()

    def frames(self):
        self.frame0 = Frame(self.janela, bg="black")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="black")
        self.frame1.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.12)
        self.frame2 = Frame(self.janela, bg="black")
        self.frame2.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.34)




