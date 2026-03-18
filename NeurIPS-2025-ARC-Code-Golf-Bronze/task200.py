def p(d):
 for s,e in enumerate(d[-1]):
  if e:
   for o in d:o[s:10:2]=[e]*((11-s)//2)
   d[0][s+1:10:4]=[5]*((12-s)//4);d[-1][s+3:10:4]=[5]*((10-s)//4);break
 return d