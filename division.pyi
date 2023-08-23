numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
residuo = numero1 % numero2
cociente = numero1 / numero2
if residuo == 0:
    print("La division de los numeros", numero1, "y el", numero2, "es exacta y su cociente es", cociente, "y su residuo es", residuo)
else:
    print("La division de los numeros", numero1, "y el", numero2, "no es exacta y su cociente es", cociente, "y su residuo es", residuo)