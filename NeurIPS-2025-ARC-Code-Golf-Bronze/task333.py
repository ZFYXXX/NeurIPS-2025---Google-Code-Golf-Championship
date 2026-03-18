def p(x):
 for _ in[0]*4:
  x=[*map(list,zip(*x[::-1]))]
  for o in x:
   if 3 in o:
    a=o.index(3);b=max(o[:a])
    if b>0:c=o.index(b);o[c:a]=[b]*(a-c)
 return x