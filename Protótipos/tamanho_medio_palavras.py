def tamanho_medio_palavras(texto):
    texto=texto .split()
    import string
    [word.strip(string.punctuation) for word in texto]
    soma_caracteres=sum(len(i) for i in texto)
    total_palavras=len(texto)
    tmp=soma_caracteres/total_palavras
    return tmp
