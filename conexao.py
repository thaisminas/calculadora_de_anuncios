import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()


class Banco:
    def __init__(self):
        pass

    def inserir(self, anuncio, cliente, data_inicio, data_termino, investimento):
        cursor.execute("""
        INSERT INTO cadastro (anuncio, cliente, data_inicio, data_termino, investimento)
        VALUES ('{}', '{}', '{}', '{}', '{}')
        """.format(anuncio, cliente, data_inicio, data_termino, investimento))
        conn.commit()
        print('Dados inseridos com sucesso')
        conn.close()

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass



