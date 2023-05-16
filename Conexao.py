import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='teste',
    user='root',
    password=''
)

cursor = conexao.cursor()

def inserir(valor, descricao):
    inserir = f"INSERT into celulares(Marca, Preco) values('{descricao}', '{valor}') "
    cursor.execute(inserir)
    conexao.commit()
    print("inserido")

def buscar_dados():
    inserir = f"select * from teste"
    cursor.execute(inserir)
    celulares = cursor.fetchall()
    return celulares

def delete(clear):
    sql = f"""DELETE FROM celulares = '{clear}';"""
    cursor.execute(sql)
    conexao.commit()

