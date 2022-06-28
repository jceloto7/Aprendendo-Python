x=int(input("Digite um número inteiro:"))
resto=x%10
while x!=0 and resto!=0:
  x=x//10
  resto=resto-x%10
if resto==0:
	print("sim")
else: 
  print("não")
  
