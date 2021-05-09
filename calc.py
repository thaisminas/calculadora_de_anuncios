# Parte 1


def visualizacoes(visualizacoes):
    cliques = 0
    #pega a quantidade de visualizaçoes que foram maior ou igual a 100
    if visualizacoes >= 100:
        #divide o total de visualizaçoes por 100
        quantidade = visualizacoes / 100
        #Pega a quantidade de visualizacoes multiplicado pela quantidade que clica nele
        cliques = quantidade * 12
        #retorna a quantidade que visualiza a cada 100 pessoas
        return round(cliques - 0.5)
    else:
        return 'Quantidade visualizada e menor que 100'

def compartilhamentos(pessoas):
    quant_compatilhamentos = 0
    clica = 0
    visualizacao_rede_compartilhada = 0
    sequencia = 0

    if pessoas >= 20:
        #Quantidade de pessoas dividido pela quantidade de cliques a cada 20
        clicam = pessoas / 20
        #quantidade de pessoas que clicam multiplicado pela quantidade de compatilhamentos
        quant_compatilhamentos = round((clicam * 3) - 0.5)
        #cada compartilhamento nas redes sociais gera 40 novas visualizações
        visualizacao_rede_compartilhada = quant_compatilhamentos * 40
        sequencia = visualizacao_rede_compartilhada * 4
        return quant_compatilhamentos + visualizacao_rede_compartilhada + sequencia
    else:
        return 'A quantidade de pessoas e menor que 20'


def valor_investimento(valor_investido):
    # 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
    anuncio_valor = (valor_investido / 1) * 30
    return round(anuncio_valor + 0.5)





projecao_maxima =






# Cadastro de Aluno

#nome_anuncio = input('Informe o nome do anuncio: ')
#cliente = input('Informe o nome do cliente: ')
#data_inicio = input('Informe data de inicio: ')
#data_termino = input('Informe data do Terminio: ')
#investimento_dia = float(input('Informe o investimento por dia: '))
