import re

def tamanho_medio_palavras(texto):
	texto=texto .split()
	soma_caracteres=sum(len(i) for i in texto)
	total_palavras=len(texto)
	tmp=soma_caracteres/total_palavras
	return tmp

def type_token(texto):
	texto=texto.lower()
	texto=texto .split()
	palavras_diferentes=list(dict.fromkeys(texto))
	soma_palavras_diferentes=len(palavras_diferentes)
	total_palavras=len(texto)
	tt=soma_palavras_diferentes/total_palavras
	return tt


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def hapax_legomana(texto):
	texto=texto .split()
	palavras_unicas=n_palavras_unicas(texto)
	total_palavras=len(texto)
	hp=palavras_unicas/total_palavras
	return hp

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def tamanho_medio_setenca(texto):
	texto=texto .split()
	setencas=separa_sentencas(texto)
	soma_caracteres=sum(len(i) for i in texto)
	total_setencas=len(setencas)
	tms=soma_caracteres/total_setencas
	return tms


