R=range
def p(g):
 N=len(g)
 for _ in R(10):
  for A in R(N):
   for B in R(N):
    if g[A][B]<1:g[A][B]=g[B][A]or g[A+1][B+1]
 return g