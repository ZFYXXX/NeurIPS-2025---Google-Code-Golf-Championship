def p(j):
 for i in range(4):
  t=j[i]
  for k in range(4):
   if t[k]>0:t[k+10]=t[k]
   elif t[k+5]>0:t[k+10]=t[k+5]
 return[r[10:]for r in j]