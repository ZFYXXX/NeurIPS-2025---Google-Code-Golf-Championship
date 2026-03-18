def p(j):
 for c in range(len(j[0])):
  f=0
  for r in range(len(j)):
   if f:j[r][c]=v
   elif j[r][c]:f=1;v=j[r][c]
 return j