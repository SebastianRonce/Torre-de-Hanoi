def mcd(a, b):
    # Caso base
    if b == 0:
        return a
    # Caso recursivo
    else:
        return mcd(b, a % b)
        

print("El MCD de 48 y 18 es:", mcd(48, 18))
print("El MCD de 56 y 98 es:", mcd(56, 98))
print("El MCD de 101 y 103 es:", mcd(101, 103))
