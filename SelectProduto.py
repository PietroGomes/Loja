import mysql.connector
import ConnectionBD as con


class Produto:
    def __init__(self, id, nome, descricao, preco, foto):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.foto = foto


def get_todos_produtos():
    listaProdutos = []
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """SELECT * FROM produto;"""
        cursor.execute(comandoSQL)
        record = cursor.fetchall()

        for i in record:
            produto = Produto(i[0], i[1], i[2], i[3], i[4])
            listaProdutos.append(produto)
    
    except mysql.connector.Error as error:
        print(f"Houve um erro: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão está fechada!")
        
        return listaProdutos
