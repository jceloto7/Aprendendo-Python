def computador (n,m):
	v= (n-m)%(m+1)
	m0=m
	while v !=0 and m!=1:
		m=m-1
		v= (n-m)%(m0+1)
	if v==0:
		print(m)
	else:
		print(m0)
