import mysql.connector
import ConnectionBD as con

class Avaliacao:
    def __init__(self, id, comentario, data, idUsuario, idProduto):
        self.idAvaliacao = id
        self.comentario = comentario
        self.data = data
        self.idUsuario = idUsuario
        self.idProduto = idProduto


def get_todas_avaliacoes(idProduto):
    listaAvaliacoes = []
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """SELECT * FROM avaliacao WHERE id_produto = %s;"""
        busca = (idProduto,)
        cursor.execute(comandoSQL, busca)
        record = cursor.fetchall()

        for i in record:
            avaliacao = Avaliacao(i[0], i[1], i[2], i[3], i[4])
            listaAvaliacoes.append(avaliacao)
    
    except mysql.connector.Error as error:
        print(f"Houve um erro: {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão está fechada!")
    
        return listaAvaliacoes
