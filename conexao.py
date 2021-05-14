import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()


class Cadastro:
    def __init__(self):
        pass

    def insert(self, anuncio, cliente, data_inicio, data_termino, investimento):
        cursor.execute("""
        INSERT INTO cadastro (anuncio, cliente, data_inicio, data_termino, investimento)
        VALUES ('{}', '{}', '{}', '{}', '{}')
        """.format(anuncio, cliente, data_inicio, data_termino, investimento))
        conn.commit()
        print('Dados inseridos com sucesso')
        conn.close()

    def consult(self):
        try:
            campo = input('Insira o registro: ')
            consulta = ('SELECT * FROM cadastro WHERE id = {}'.format(campo))
            cursor.execute(consulta)
            conn.commit()
            linhas = cursor.fetchone()

            for linha in linhas:
                print(linha)

        except Exception as erro:
            print('Falha ao consultar tabela: {}'. format(erro))
        finally:
            conn.close()

    def deleteById(self):
        try:
            campo = input('Insira o registro para deletar: ')
            apagar = ('DELETE FROM cadastro WHERE id = {}'.format(campo))
            cursor.execute(apagar)
            conn.commit()

        except Exception as erro:
            print('Falha ao deletar campo: {}'.format(erro))
        finally:
            conn.close()

    def deleteByName(self):
        try:
            campo = input('Insira o registro para deletar: ')
            apagar = ('DELETE FROM cadastro WHERE cliente = {}'.format(campo))
            cursor.execute(apagar)
            conn.commit()

        except Exception as erro:
            print('Falha ao deletar campo: {}'.format(erro))
        finally:
            conn.close()


    def get(self):
        pass

    def update(self):
        pass




