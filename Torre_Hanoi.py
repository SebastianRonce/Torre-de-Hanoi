def hanoi(n, inc="1", aux="2", fin="3"):
    if n > 0:
        hanoi(n - 1, inc, fin, aux)
        print(f"Mover disco {n} de {inc} a {fin}")
        hanoi(n - 1, aux, inc, fin)
