def p(d):
 for i in range(1,len(d)):
  for j in range(len(d)-1):d[i][j]=2*(d[i][-1]==d[0][j]==5)
 return d