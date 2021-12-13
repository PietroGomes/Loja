import mysql.connector
import ConnectionBD as con

def inserir_produto(nome, descricao, preco, urlFoto):
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """INSERT INTO produto(nome, descricao, preco, foto) VALUES(%s, %s, %s, %s);"""
        record = (nome, descricao, preco, urlFoto)
        cursor.execute(comandoSQL, record)
        connection.commit()
        print("Produto cadastrado!")

    except mysql.connector.Error as error:
        print(f"Houve um erro ao cadastrar o produto! {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o banco foi fechada!")
