R=range
def p(g):
 B=sum(g,[]);A=B.count(0);C=[[0]*(A*3)for _ in R(A*3)]
 for D in R(9-A):
  for i in R(9):
   if g[i//3][i%3]:C[i//3+D//A*3][i%3+D%A*3]=max(B)
 return C