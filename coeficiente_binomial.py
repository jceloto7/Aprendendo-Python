n=int(input("Digite o valor de n:"))
k=int(input("Digite o valor de k:"))
def fatorial(x):
  n=x
  v=1
  n_fat=1
  while v<=n:
   n_fat=n_fat*v
   v=v+1
  return n_fat 
n_fat=fatorial(n)
k_fat=fatorial(k)
nk_fat=fatorial((n-k))
cb=n_fat/(k_fat*nk_fat)
print(cb)