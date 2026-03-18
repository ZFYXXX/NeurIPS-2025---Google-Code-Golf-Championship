def p(j):
 c,e=divmod(sum(j,[]).index(2),5)
 j[c][e]=0
 if c*e:j[c-1][e-1]=3
 if (c<2)*e:j[c+1][e-1]=8
 if (e<4)*c:j[c-1][e+1]=6
 if c<2 and e<4:j[c+1][e+1]=7
 return j