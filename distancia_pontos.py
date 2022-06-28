import math
x1=int(input("Digite o valor de x do primeiro ponto:"))
y1=int(input("Digite o valor de y do primeiro ponto:"))
x2=int(input("Digite o valor de x do segundo ponto:"))
y2=int(input("Digite o valor de y do segundo ponto:"))
d=math.sqrt((x1-x2)**2+(y1-y2)**2) 
if d >=10:
  print("longe")
else:
  print("perto")