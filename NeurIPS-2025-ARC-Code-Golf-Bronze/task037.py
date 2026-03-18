def p(e):
	u={}
	for n,r in enumerate(e):
		for p,i in enumerate(r):
			if i:u[i]=u.get(i,[])+[(n,p)]
	for i in u:
		(n,p),(r,d)=u[i];a,d=(r>n)-(r<n),(d>p)-(d<p)
		for s in range(abs(r-n)+1):e[n+s*a][p+s*d]=i
	return e