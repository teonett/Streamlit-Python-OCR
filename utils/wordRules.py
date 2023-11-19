import re

def calcula_percentual(quantidade, tamanho):
    """Funcao para calcular o percentual de palavras boas/mas.
    \nRetorna float, o percentual.
    \nEx.:
    quantidade = quantidade de palavras boas/mas
    tamanho = quantidade de palavras do texto
    percentual = calcula_percentual(quantidade, tamanho)"""
    percentual = (quantidade / tamanho) * 100
    return percentual

def buscar_palavras_mas(texto):
    """Funcao para buscar palavras 'mas' (mau) no texto extraido.
    \nDespreza as palavras repetidas. Retorna um int, float.
    \nRespectivamente a quantidade de palavras mas encontradas e o percentual delas no texto todo.
    \nEx.:
    texto = texto extraido da imagem
    quantidade, percentual = buscar_palavras_mas(texto)"""
    cont_mau = 0
    palavras_mas = open("utils/wordsArrayBad.txt").read()
    palavras_mas = palavras_mas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_mas:
            cont_mau += 1
    percentual = calcula_percentual(cont_mau, len(palavras_texto))

    return cont_mau, percentual


def buscar_palavras_boas(texto):
    """Funcao para buscar palavras de 'bem' no texto extraido.
    \nDespreza as palavras repetidas. Retorna um int, float.
    \nRespectivamente a quantidade de palavras boas encontradas e o percentual delas no texto todo.
    \nEx.:
    texto = texto extraido da imagem
    quantidade, percentual = buscar_palavras_boas(texto)"""
    cont_bem = 0
    palavras_boas = open("utils/wordsArrayGood.txt").read()
    palavras_boas = palavras_boas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_boas:
            cont_bem += 1
    percentual = calcula_percentual(cont_bem, len(palavras_texto))

    return cont_bem, percentual