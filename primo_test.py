def primo(n):
  cont = 0
  i = 0
  while i <= n or cont < 2:
    i = i + 1
    x = n % i
    if x == 0:
      cont = cont + 1
  if cont <= 2:
    return("primo")
  else:
    return("não primo")

def test_1():
	assert primo(7)=="primo"
def test_2():
	assert primo(25)=="não primo"
def test_3():
	assert primo(1)=="não primo"   	
def test_4():
	assert primo(2)=="primo"
def test_5():
	assert primo(3)=="primo"	
def test_6():
	assert primo(4)=="não primo"
def test_7():
	assert primo(11)=="primo"
def test_8():
	assert primo(6)=="primo"	
