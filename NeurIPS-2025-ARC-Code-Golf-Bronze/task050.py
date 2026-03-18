def p(c):
 g=[*map(list,c)]
 for _ in 0,1:
  for r in g:
   i=-1
   while 1:
    try:i=r.index(8,i+1);j=r.index(8,i+1);r[i+1:j]=[3]*(j-i-1)
    except:break
  g=[*map(list,zip(*g))]
 return g