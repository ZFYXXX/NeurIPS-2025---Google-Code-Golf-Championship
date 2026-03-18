def p(t):
 for y in t:g=0;y[:]=[(g:=x if x>0 else g)for x in y]
 g=0
 for y in t:y[-1]=g=y[-1] if y[-1]>0 else g
 return t