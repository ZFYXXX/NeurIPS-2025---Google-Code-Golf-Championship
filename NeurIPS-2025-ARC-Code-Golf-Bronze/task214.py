def p(g,R=range):
 for A in R(3):
  for B in R(3):g[A][B+4]=g[~B][A];g[A][B+8]=g[~A][2-B]
 return g