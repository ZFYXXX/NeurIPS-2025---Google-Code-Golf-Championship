def p(g):
 a=[0]*10;r=range(10)
 for i in r:
  for j in r:
   if v:=g[i][j]:a[v]=g[i].count(v)*sum(t[j]==v for t in g)
 return[[a.index(max(a))]*2]*2