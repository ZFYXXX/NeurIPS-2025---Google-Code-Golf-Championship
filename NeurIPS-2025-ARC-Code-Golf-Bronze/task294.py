def p(g):
 for k in range(64):
  i=k//8+1;j=k%8+1
  if g[i+1][j]*g[i][j+1]*g[i-1][j]*g[i][j-1]:g[i][j]=2
 return g