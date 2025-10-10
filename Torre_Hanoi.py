def hanoi(n, inc="Ini", aux="Axi", fin="Fin"):
    if n > 0:
        # Paso 1: Mover n-1 discos de la torre inicial a la auxiliar
        hanoi(n - 1, inc, fin, aux)
        # Paso 2: Mover el disco más grande de la inicial a la final
        print(f"Mover disco {n} de {inc} a {fin}")
        # Paso 3: Mover n-1 discos de la auxiliar a la final
        hanoi(n - 1, aux, inc, fin)


print("=== Torre de Hanoi ===")
print("Para iniciar, oprima cualquier tecla.")
print("Para salir, oprima 0.")
opción = input()
while opción != "0":
    try:
        discos = int(input("Ingrese el número de discos (máximo 10): "))
            # Validar que el número sea válido
        if discos == 0:
            print("Saliendo del programa.")
            break
        elif discos < 1 or discos > 10:
            print("Error: El número de discos debe estar entre 1 y 10.")
        else:
            # Resolver la Torre de Hanoi
            print(f"\nResolviendo Torre de Hanoi con {discos} discos:")
            hanoi(discos)
            print(f"\nEl número mínimo de movimientos es: {2**discos - 1}")
    except ValueError:
        # Capturar error si el usuario no ingresa un número
        print("Error: Debe ingresar un número entero válido")
    except Exception as e:
        # Capturar cualquier otro error inesperado
        print(f"Error inesperado: {e}")

