def p(g):
 R=range;Z=[r[:]for r in g]
 for r in R(1,len(g),4):
  for c in R(1,len(g[0]),4):
   for i in R(9):Z[r-1+i//3][c-1+i%3]=g[r][c]+5
 return Z