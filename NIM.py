def usuario_escolhe_jogada(n,m):
	u=int(input("Quantas peças você vai tirar?"))
	if u <= m and u>0:
		print("Você retirou",u,"peças.")
		return u
	while u >m or u <=0:
		u=int(input("Jogada inválida.Por favor tente de novo.Quantas peças você vai tirar?"))
	print("Você retirou",u,"peças.")
	return u

def computador_escolhe_jogada(n,m):
	v= (n-m)%(m+1)
	m0=m
	while v !=0 and m!=1:
		m=m-1
		v= (n-m)%(m0+1)
	if v==0:
		print("O computador retirou", m, "peças.")
		return m
	else:
		print("O computador retirou", m0, "peças.")
		return m0

def partida():
	n= int(input("Escolha qual será o número inicial de peças na mesa:"))
	m= int(input("Escolha o número máximo de peças a serem retiradas por rodada:"))
	if n%(m+1)==0:
		print("Você começa!")
		while n>0:
			n=n-usuario_escolhe_jogada(n,m)
			print("Agora sobraram",n,"na mesa.")
			if n>0:
				n=n-computador_escolhe_jogada(n,m)
				print("Agora sobraram",n,"na mesa.")
				if n==0:
					print("Fim do jogo.O computador ganhou!")
			else:
				print("Fim do jogo.Você ganhou!")

	else:
		print("Computador começa!")
		while n>0:
			n=n-computador_escolhe_jogada(n,m)
			print("Agora sobraram",n,"na mesa.")
			if n>0: 	
				n=n-usuario_escolhe_jogada(n,m)
				print("Agora sobraram",n,"na mesa.")
				if n==0:
					print("Você ganhou!") 
			else:
				print("O computador ganhou!")
def campeonato():
	print("Rodada 1")
	partida()
	print("Rodada 2")
	partida()
	print("Rodada 3")
	partida()
	print("Final do campeonato!")
	print("Placar: Você 0 x 3 Computador")

print("Bem vindo ao jogo do NIM!Escolha:")
print()
print("1- para jogar uma partida isolada")
x=int(input("2- para jogar um campeonato:"))
print()
if x==1:
	print("Você escolheu uma partida isolada.")
	partida()
if x==2: 
	print("Você escolheu um campeonato.") 
	campeonato()	
partida()