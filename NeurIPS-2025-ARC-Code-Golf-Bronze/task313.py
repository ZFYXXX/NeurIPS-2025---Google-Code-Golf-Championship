def p(e,r=range,n=len):
 j=n(e);y=n(set(e[0]))-1;q=n({p[0]for p in e})-1
 for p in e:p[:]=p[:y]*(n(p)//y)+p[:n(p)%y]
 for h in r(j):e[h]=e[h%q][:j]
 return[[e[0][e[0].index(p)+1]for p in p]for p in e]