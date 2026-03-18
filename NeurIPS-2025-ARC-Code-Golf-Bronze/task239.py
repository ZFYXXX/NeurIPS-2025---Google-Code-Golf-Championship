from collections import*
def p(s):m=Counter(sum(s,[])).most_common(9);return[[(e,0)[r>=c]for e,c in m]for r in range(m[0][1])]