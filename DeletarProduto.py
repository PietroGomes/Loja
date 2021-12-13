import mysql.connector
import ConnectionBD as con

def delete_produto_id(id):
    try:
        connection = con.connectionBD()
        cursor = connection.cursor()
        comandoSQL = """DELETE FROM produto WHERE id = %s;"""
        record = (id,)
        cursor.execute(comandoSQL, record)
        connection.commit()
        print("Produto excluído!")

    except mysql.connector.Error as error:
        print(f"Houve um erro ao deletar o produto: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão do MySQL está fechada!")
