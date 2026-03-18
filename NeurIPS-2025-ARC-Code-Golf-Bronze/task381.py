def p(t,q=range):
 s=len(t)
 for o in q(1,s-1):
  n=p=0
  for r in q(s):
   d=t[o][r];n=[n,1][n<1<d]
   if n==1>d:n=2;p=[p,r][~p]
   if n>1<d:
    for r in q(p,r):t[o][r]=9;n=1;p=0
 return t