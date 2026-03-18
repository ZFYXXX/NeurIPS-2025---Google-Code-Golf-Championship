def p(n):
 h=len(n);w=len(n[0]);c=n[0].index(7);l=0
 while l<h and n[l][c]==7:l+=1
 for i in range(l):
  for j in range(max(0,c-l+1+i),min(w,c+l-i)):n[i][j]=7+(j-c)%2
 return n