z=lambda g:[*map(list,zip(*g[::-1]))]
p=lambda g:(h:=[a+b for a,b in zip(g,z(g))])+z(z(h))