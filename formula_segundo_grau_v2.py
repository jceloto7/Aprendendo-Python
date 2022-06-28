import math
a=float(input("Digite o valor de a:"))
b=float(input("Digite o valor de b:"))
c=float(input("Digite o valor de c:"))
def delta(a,b,c):
	return b**2-(4*a*c)	
d=delta(a,b,c)	
def positivo (a,b,c):
	return(-b+math.sqrt(d))/(2*a)
def negativo (a,b,c):
	return(-b-math.sqrt(d))/(2*a)
if d<0:
  print("esta equação não possui raízes reais")  
if d==0:
  x1=positivo(a,b,d) 	   
  print("a raiz desta equação é",x1)
if d>0:
  x1=positivo(a,b,d) 
  x2=negativo(a,b,d)
  if x1>x2:
   print("as raízes da equação são",x2,"e",x1) 
  else:
   print("as raízes da equação são",x1,"e",x2)