def hanoi(n, inc="1", aux="2", fin="3"):
    if n > 0:
        hanoi(n - 1, inc, fin, aux)
        print(f"Mover disco {n} de {inc} a {fin}")
        hanoi(n - 1, aux, inc, fin)
discos = int(input("Ingrese el número de discos: "))
hanoi(discos)
print("El número mínimo de movimientos es:", 2**discos - 1)
