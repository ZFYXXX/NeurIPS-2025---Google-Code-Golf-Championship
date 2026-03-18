def p(j,A=enumerate):
 c,E=zip(*((i,c)for i,r in A(j)for c,v in A(r)if v))
 for k,w in zip([0,-1,1,0,0],[0,0,0,-1,1]):j[sum(c)//2+k][sum(E)//2+w]=3
 return j