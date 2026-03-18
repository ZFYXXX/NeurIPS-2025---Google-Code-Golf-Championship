def p(o):
 n=len(o);g=[[0]*n for _ in' '*n];x,y=-1,0;u,v=1,0
 for l in[n]+[k for k in range(n-1,0,-2)for _ in'  ']:
  for _ in [0]*l:x+=u;y+=v;g[y][x]=3
  u,v=-v,u
 return g