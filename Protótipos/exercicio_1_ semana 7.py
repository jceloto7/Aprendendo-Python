largura_fixa=int(input("digite a largura:"))
altura_fixa=int(input("digite a altura:"))
largura_variavel=1
altura_variavel=1
retangulo="#"
while altura_variavel<=altura_fixa:
	while largura_variavel<=largura_fixa:
		retangulo="#"+"#"
		largura_variavel=largura_variavel+1
	print()
	largura_variavel=1
	altura_variavel=altura_variavel+1
print(retangulo)
	
