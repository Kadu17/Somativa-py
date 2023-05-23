from tkinter import ttk, Tk
from tkinter import *
import tkinter.font as tkFont

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.lista_marcas()
        self.labels()
        self.lista_tudo()
        self.janela.mainloop()


    def tela(self):
        self.janela.title("Web Scrapping")
        self.janela.configure(background="lightBlue")
        self.janela.geometry("600x700")
        self.janela.resizable(True, True)
        self.janela.minsize(width=300, height=500)


    def frames(self):
    #     self.frame0 = Frame(self.janela, bg="black")
    #     self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
    #     self.frame1 = Frame(self.janela, bg="black")
    #     self.frame1.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.12)
        self.frame2 = Frame(self.janela, bg="black")
        self.frame2.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.34)

    def botoes(self):
        self.btWeb = Button(text='Web Scraping', background='#f7f8f7')
        self.btWeb.place(relx=0.05, rely=0.10, relwidth=0.18, relheight=0.04)
        self.btBuscar = Button(text='Buscar', background='#f7f8f7')
        self.btBuscar.place(relx=0.25, rely=0.10, relwidth=0.10, relheight=0.04)
        self.btLimpar = Button(text='Limpar', background='#f7f8f7')
        self.btLimpar.place(relx=0.859, rely=0.10, relwidth=0.10, relheight=0.04)

    def labels(self):
        self.titulo = Label(text="WEB SCRAPPING", background="lightblue", foreground='black')
        self.titulo.place(relx=0.38, rely=0.03)
        fontReal = tkFont.Font(family="Arial", size=16, weight="bold", )
        self.titulo.configure(font=fontReal)

    def lista_marcas(self):
        clicked = StringVar()
        self.drop = OptionMenu(janela, clicked, "Apple", "Samsung", "Xiaomi", "Motorola")
        self.drop.pack()
        self.drop.place(relx=0.55, rely=0.10, relwidth=0.25, relheight=0.04)
        clicked.set( "Marcas" )

    def lista_tudo(self):
        self.lista = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))

        self.lista.heading('#0', text='ID')
        self.lista.heading('#1', text='Marca')
        self.lista.heading('#2', text='Modelo')
        self.lista.heading('#3', text='Preço')

        self.lista.column('#0', width=50)
        self.lista.column('#1', width=195)
        self.lista.column('#2', width=270)
        self.lista.column('#3', width=100)

        self.lista.place(relx=0.025, rely=0.080, relwidth=0.950, relheight=0.850)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.lista.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.952, rely=0.079, relwidth=0.02, relheight=0.84)


