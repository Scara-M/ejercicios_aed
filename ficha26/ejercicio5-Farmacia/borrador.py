def add_in_order(v,art):
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2
        
        if art.nombre == v[c].nombre:
            pos = c
            break
        if art.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [art]

v = []
art = ["Ana", "Tomas", "David", "Luis"]
art = ["Ana", "fUIG", "David", "Luis"]
add_in_order(v,art)
print(v)