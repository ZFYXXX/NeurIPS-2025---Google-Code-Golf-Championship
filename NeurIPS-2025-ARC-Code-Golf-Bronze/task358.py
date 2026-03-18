def p(g):
 for _ in[0]*4:
  g=[*map(list,zip(*g[::-1]))]
  for r in g:
   if len({*r})>2:b=[x for x in r if x>0];c=r.index(b[0])%len(b);r[:]=(b[-c:]+b*20)[:len(r)]
 return g