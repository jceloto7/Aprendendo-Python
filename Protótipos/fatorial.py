x=int(input("Digite o valor de n:"))
if x==0:
  print("1") 
if x>0:
   y=x-1
   while y>0:
    x=x*y
    y=y-1
print(x)