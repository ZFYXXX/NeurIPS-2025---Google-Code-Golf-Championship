def p(f):
 i,l=len(f),len(f[0]);b,e,a,t=i,0,l,0
 for r in range(i):
  for p in range(l):
   if f[r][p]-1:b,e,a,t=min(b,r),max(e,r),min(a,p),max(t,p)
 return[[g-(g==1)for g in g[a:t+1]]for g in f[b:e+1]]