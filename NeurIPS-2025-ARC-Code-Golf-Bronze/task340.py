z=range
def p(g):
 f=[]
 for _ in z(4):
  g=[*map(list,zip(*g[::-1]))]
  for i in g[1:-1]:
   f+=[d:=i[0]];t=1
   for r in z(1,len(i)-1):
    if i[r]==d:i[t]=d;i[r]=0;t+=1
 return[[i*(i in f)for i in i]for i in g]