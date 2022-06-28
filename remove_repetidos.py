def remove_repetidos(lista):
	lista=list(dict.fromkeys(lista))
	list.sort(lista)
	return lista