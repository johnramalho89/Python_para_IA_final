def o_maior_numero(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


def o_maior_numero2(a, b, c):
    return max(a, b, c)

print(o_maior_numero(60,20,30))

o_maior_numero2(50,14,90)