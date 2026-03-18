def p(g):
 g=[10*[r[0]]for r in g*3 if r.count(0)<2]
 for i in range(10):
  for j in range(10):g[i][j]=g[j][i]
 return g[:10]