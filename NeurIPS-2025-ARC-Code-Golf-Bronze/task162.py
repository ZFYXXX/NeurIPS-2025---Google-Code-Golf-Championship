def p(j,A=range(18)):
 for c in A:E,k,W=j[c:c+3];[exec("E[l:J]=k[l:J]=W[l:J]=[1]*3")for l in A if sum(E[l:(J:=l+3)]+k[l:J]+W[l:J])==0]
 return j