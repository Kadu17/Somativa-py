import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='teste',
    user='root',
    password=''
)

cursor = conexao.cursor()
cursor.execute('select database();')
dados = cursor.fetchall()
print(dados)
