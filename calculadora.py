# Parte 1

valor_investido = float(input('Informe o valor do investimento: '))


def calcula_visualizacoes(visualizacoes):
    cliques = 0
    if visualizacoes >= 100:
        quantidade = visualizacoes / 100
        cliques = quantidade * 12
    return round(cliques - 0.5)


def compartilhamento_redes(pessoas):
    quant_compatilhamentos = 0
    clica = 0
    visualizacao_rede_compartilhada = 0
    sequencia = 0

    if pessoas >= 20:
        quant_compatilhamentos = pessoas / 20
        clicam = round((quant_compatilhamentos * 3) - 0.5)
        visualizacao_rede_compartilhada = clicam * 40
        sequencia = visualizacao_rede_compartilhada * 4
        return clicam, visualizacao_rede_compartilhada, sequencia
    else:
        return 'O valor e menor que 20'



def valor_investimento(valor_investido):
    anuncio_valor = (valor_investido / 1) * 30
    return round(anuncio_valor + 0.5)













# Cadastro de Aluno

#nome_anuncio = input('Informe o nome do anuncio: ')
#cliente = input('Informe o nome do cliente: ')
#data_inicio = input('Informe data de inicio: ')
#data_termino = input('Informe data do Terminio: ')
#investimento_dia = float(input('Informe o investimento por dia: '))
