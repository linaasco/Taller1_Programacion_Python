a = input("Ingrese un numero o una letra puede ser en minuscula o mayuscula")
representacion = ord(a)
if representacion >= 48 and representacion < 58:
    print("El caracter", a, "es un numero")
elif representacion >= 65 and representacion < 91:
    print("El caracter", a, "es una letra mayuscula")
elif representacion >= 97 and representacion < 123:
    print("El caracter", a, "es una letra minuscula")
else:
    print("El caracter no es ni una letra y suma")