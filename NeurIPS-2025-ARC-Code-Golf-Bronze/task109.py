q=range
def p(t):
 l=len(t);m=l//2;p=t[0][m];n=[[0]*(l-1)for _ in q(l-1)]
 for r in q(m):
  u=~r
  for c in q(m):d=~c;a=p*(t[r][c]>0);n[r][c]=n[u][c]=n[u][d]=n[r][d]=a
 return n