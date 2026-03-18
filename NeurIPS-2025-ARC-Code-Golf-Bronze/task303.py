def p(j,A=range):
 r,c=len(j),len(j[0])
 for i in A(r):
  if sum(j[i])==0:j[i]=[2]*c
 for i in A(c):
  if all(r[i]in[0,2]for r in j):
   for r in j:r[i]=2
 return j