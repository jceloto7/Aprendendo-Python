def primo(k):
  cont = 0
  i = 0
  while i <= k or cont < 2:
    i = i + 1
    x = k % i
    if x == 0:
      cont = cont + 1
  if cont <= 2:
    return("primo")
  else:
    return("não primo")

def maior_primo(n):  
  x=n
  if primo(n) =="primo":
    return n
  while x!= "primo":
    n=n-1
    x=primo(n)
  return n  

def test_1():
  assert maior_primo(100)==97
def test_2():
  assert maior_primo(7)==7
def test_3():
  assert maior_primo(2)==2
def test_4():
  assert maior_primo(2431)==2423           