def vogal (v):
    if v in "aeiouAEIOU":
        return True
    else:
        return False

def test_1():
	assert vogal("j")==False  
def test_2():
	assert vogal("a")==True
def test_3():
	assert vogal("O")==True        