import mysql.connector


def connectionBD():
    meuBanco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "loja"
    )
    return meuBanco
