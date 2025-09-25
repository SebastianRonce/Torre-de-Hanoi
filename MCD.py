def mcd(a, b):
    # Caso base
    if b == 0:
        return a
    # Caso recursivo
    else:
        return mcd(b, a % b)

print(mcd(48, 18))  
print(mcd(56, 98))  
print(mcd(101, 103)) 