def p(i,r=range):
 L=len(i);l=sum(i[d][h]==i[d][h+1]==i[d+1][h]==i[d+1][h+1]==2for d in r(L-1)for h in r(L-1));d=[[0]*3for _ in r(3)]
 for h in r(l):d[h*2//3][h*2%3]=1
 return d