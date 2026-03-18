def p(p):
 a=[*map(list,p)]
 for i in range(9):
  for m in range(4,13):
   if p[i][m]:
    for q in-1,0,1:
     for g in-1,0,1:
      if 0<=i+q<9and 4<=m+g<13:a[i+q][m+g]=p[q+1][g+1]
 return a