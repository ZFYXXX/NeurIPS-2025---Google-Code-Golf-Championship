def p(g):
	for A in range(6):
		if g[A][0]|g[A][5]:g[A]=[2]*6;B=A
		if g[0][A]|g[5][A]:
			for C in g:C[A]=8;D=A
	g[B][D]=4;return g