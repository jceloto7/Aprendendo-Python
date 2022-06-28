import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

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

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_palavras(texto):
    texto .split()
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

def hapax_legomana(texto):
    texto=texto .split()
    palavras_unicas=n_palavras_unicas(texto)
    total_palavras=len(texto)
    hp=palavras_unicas/total_palavras
    return hp    

def tamanho_medio_setenca(texto):
    setencas=separa_sentencas(texto)
    texto= texto.split()
    soma_caracteres=sum(len(i) for i in texto)
    total_setencas=len(setencas)
    tms=soma_caracteres/total_setencas
    return tms

def complexidade_setenca(texto):
    setencas=separa_sentencas(texto)
    total_setencas=len(setencas)
    frases=separa_frases(texto)
    total_frases=len(frases)
    cs=total_frases/total_setencas
    return cs

def tamanho_medio_frase(texto):
     frases=separa_frases(texto)
     soma_caracteres_frases=sum(len(i) for i in frases)
     total_frases=len(frases)
     tmf=soma_caracteres_frases/total_frases
     return tmf


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tmp = tamanho_medio_palavras(texto)
    tt=type_token(texto)
    hl=hapax_legomana(texto)
    tms=tamanho_medio_setenca(texto)
    cs=complexidade_setenca(texto)
    tmf=tamanho_medio_frase(texto)
    resultado=[tmp,tt,hl,tms,cs,tmf]
    return resultado
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass