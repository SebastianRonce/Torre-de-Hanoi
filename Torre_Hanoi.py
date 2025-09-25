def hanoi(n, inc="I", aux="A", fin="F"):
    if n > 0:
        # Paso 1: Mover n-1 discos de la torre inicial a la auxiliar
        hanoi(n - 1, inc, fin, aux)
        # Paso 2: Mover el disco más grande de la inicial a la final
        print(f"Mover disco {n} de {inc} a {fin}")
        # Paso 3: Mover n-1 discos de la auxiliar a la final
        hanoi(n - 1, aux, inc, fin)

