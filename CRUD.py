import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '12345',
    database = 'practice',
)
cursor = conexao.cursor()

# CRUD

# CREATE
nome_produto = "produto1"
valor = 15
comando = f'INSERT INTO bdpractice (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # Para editar o Banco de Dados

# READ
comando = f'SELECT * FROM bdpractice'
cursor.execute(comando)
resultado = cursor.fetchall() # Para ler o Banco de Dados
print (resultado)

# UPDATE
nome_produto = "produto2"
valor = 6
comando = f'UPDATE bdpractice SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # Para editar o Banco de Dados

# DELETE
nome_produto = "produto2"
comando = f'DELETE FROM bdpractice WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # Para editar o Banco de Dados

cursor.close()
conexao.close()