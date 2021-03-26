num = int ( input("Ingresá un número: "))

if num % 2 == 0:
    print("Es multiplo de 2")
elif num % 3 == 0:
    print("Es multiplo de 3")
elif num % 5 == 0:
    print("Es multiplo de 5")
else:
    print("No es multiplo de 2, ni de 3, ni de 5")
input("Presione una tecla para salir")
