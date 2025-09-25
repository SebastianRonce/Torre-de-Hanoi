def mcd(a, b):
    # Caso base
    if b == 0:
        return a
    # Caso recursivo
    else:
        return mcd(b, a % b)

# Ejemplo de uso
print(mcd(48, 18))  # Resultado esperado: 6
print(mcd(56, 98))  # Resultado esperado: 14
print(mcd(101, 103))  # Resultado esperado: 1