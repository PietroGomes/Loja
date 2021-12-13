import mysql.connector
import ConnectionBD as con
from datetime import datetime

def inserir_avaliacao(comentario, idUser, idProduto):
    data = datetime.today().strftime('%Y-%m-%d')
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """INSERT INTO avaliacao(comentario, data_avaliacao, id_usuario, id_produto) VALUES(%s, %s, %s, %s);"""
        record = (comentario, data, idUser, idProduto)
        cursor.execute(comandoSQL, record)
        connection.commit()
        print("Avaliação cadastrada!")

    except mysql.connector.Error as error:
        print(f"Houve um erro ao cadastrar a avaliação! {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o banco foi fechada!")
