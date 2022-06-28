palmeiras=int(input("Digite o valor de n:"))
corinthians=palmeiras+1
bragantino=corinthians
santos=corinthians
while bragantino >0:
  bragantino=bragantino-1
  santos=santos*bragantino
flamengo=santos/corinthians
if flamengo ==0:
	print(1)
else:
	print(flamengo)