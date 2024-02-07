pintas=["picas","treboles","diamantes","corazones"]
valores=["A","J","Q","K"]+ [str(i) for i in range(2,11)]
mazo=[(U,P) for U in valores for P in pintas]
for c in mazo:
    print(c)