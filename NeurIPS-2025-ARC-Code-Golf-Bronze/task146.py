def p(g):
 for i in(0,3,6):
  a=g[i:i+3]
  if [*map(tuple,a)]!=[*zip(*a)]:return a