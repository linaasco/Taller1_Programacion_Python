lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))
lado3 = int(input("Ingrese el valor del lado 3: "))



if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triangulo isosceles")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Es un triangulo escaleno")
else:
    print("El triangulo es invalido")