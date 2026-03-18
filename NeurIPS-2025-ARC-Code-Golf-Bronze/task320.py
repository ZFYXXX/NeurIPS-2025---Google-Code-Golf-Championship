def p(j,A=range):
 c=len(j);E=len(j[0]);p=[x[:]for x in j]
 for k in A(E):
  W=[i for i in A(c)if j[i][k]]
  for J in A(len(W)//2):p[W[~J]][k]=8
 return p