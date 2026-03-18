def p(g,r=range):
 a=[[0]*3for i in r(3)]
 for i in r(81):
  val=g[i//9][i%9]
  if val!=5:a[i//27][i%9//3]=val
 return a