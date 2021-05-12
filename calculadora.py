# Parte 1

class Calculadora:

    def __init__(self, visualizacoes, pessoas, valor_investido):
        self.visualizacoes = visualizacoes
        self.pessoas = pessoas
        self.valor_investido = valor_investido

    def get_visualizacoes(self):
        cliques = 0
        #pega a quantidade de visualizaçoes que foram maior ou igual a 100
        if self.get_visualizacoes >= 100:
            #divide o total de visualizaçoes por 100
            quantidade = self.get_visualizacoes / 100
            #Pega a quantidade de visualizacoes multiplicado pela quantidade que clica nele
            return int(quantidade) * 12
        else:
            return 'Quantidade visualizada e menor que 100'

    def compartilhamentos(self):
        quant_compatilhamentos = 0
        clica = 0
        visualizacao_rede_compartilhada = 0
        sequencia = 0

        if self.pessoas >= 20:
            #Quantidade de pessoas dividido pela quantidade de cliques a cada 20
            clicam = self.pessoas / 20
            #quantidade de pessoas que clicam multiplicado pela quantidade de compatilhamentos
            quant_compatilhamentos = int(clicam) * 3
            #cada compartilhamento nas redes sociais gera 40 novas visualizações
            visualizacao_rede_compartilhada = quant_compatilhamentos * 40

            if visualizacao_rede_compartilhada >= 100:
                 self.get_visualizacoes = visualizacao_rede_compartilhada
                 self.get_visualizacoes()

            if quant_compatilhamentos <= 4:
                 self.compartilhamentos()

            return visualizacao_rede_compartilhada
        else:
            return 'A quantidade de pessoas e menor que 20'

    def valor_investimento(self):
        # 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
        anuncio_valor = float(self.valor_investido / 1) * 30
        return round(anuncio_valor + 0.5)


cal = Calculadora(100, 20, 30)
print(cal.compartilhamentos())
print(cal.valor_investimento())

