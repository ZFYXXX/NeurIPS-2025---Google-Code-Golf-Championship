def p(g):
 n=len(g)
 for D in [g[::-1],[r[::-1]for r in g]]:
  for i in range(n):
   for j in range(n):
    if g[i][j]==4:g[i][j]=D[i][j]
 return g