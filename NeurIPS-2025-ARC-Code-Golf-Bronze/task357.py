def p(g):
 B,D=len(g),len(g[0]);g=[[8]*D for _ in g];L=max(1,2*D-2)
 for C in range(B):i=C%L;g[~C][min(i,2*D-2-i)]=1
 return g