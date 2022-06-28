def maximo(x,y):
  n=x-y
  if n>0:
   return (x)
  else:
   return (y)
   
#testes

def test_1():
  assert maximo(7,5) ==7

def test_2():
  assert maximo(-8,-13) ==-8

def test_3():
  assert maximo(-13,-8) ==-8

def test_4():
  assert maximo(5,7) == 7

def test_5():
	assert maximo(-10,5)==5

def test_6():
	assert maximo(5,-10)==5
def test_7():
	assert maximo(-10,-10)==-10 