número=int(input("Digite um número inteiro:"))
resto1=número%3
resto2=número%5
if resto1==0 and resto2==0:
  print("FizzBuzz")
else:
  print(número)