a=int(input("Digite um número primo:"))
'''Aqui a pessoa digitou o número e este número foi transformado na variável "a"'''
 b=2
 '''O "b" é o divisor inicial. Toda verificação de números primos é iniciada pelo divisor "2".'''  
c=a
'''Apenas um valor para a função abaixo não dar erro. A variável "c" sempre será o resultado das divisões.'''
while c!=1:
	c=a/b
'''	Enquanto o "c" não for igual a "1" a operação será continuada em loop.'''
	if c==int:
		d=b
	if c== float:
		b=b+1
			