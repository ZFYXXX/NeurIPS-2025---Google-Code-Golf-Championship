def p(q,p=enumerate):
 for e,x in p(q):
  for k,n in p(x):
   if n==1:
    if e>0:q[e-1][k]=2
    if e<9:q[e+1][k]=8
    if k>0:q[e][k-1]=7
    if k<9:q[e][k+1]=6
 return q