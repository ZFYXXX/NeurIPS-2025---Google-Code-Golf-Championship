def p(r):
 a=[*map(list,r)]
 for i in range(1,len(r)):
  for j in range(1,len(r[0])-1):
   if r[i][j]==0 and (x:=r[i][j-1]) and x==r[i][j+1]==r[i-1][j]:a[-1][j]=4
 return a