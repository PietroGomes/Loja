import mysql.connector
import ConnectionBD as con

def delete_avaliacao_id(id):
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """DELETE FROM avaliacao WHERE id = %s;"""
        record = (id,)
        cursor.execute(comandoSQL, record)
        connection.commit()
        print("Avaliação excluída!")
    
    except mysql.connector.Error as error:
        print(f"Houve um erro ao deletar a avaliação: {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o banco foi fechada!")
