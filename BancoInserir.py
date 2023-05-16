import mysql.connector
cursor = 0

try:
    conexao = mysql.connector.connect(
        host='localhost',
        database='teste',
        user='root',
        password=' '
    )
except Exception as error:
    print(error)
else:
    cursor = conexao.cursor()
