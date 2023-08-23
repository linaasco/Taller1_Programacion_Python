anno = int(input("Ingrese el anno\n"))
division = anno % 400
division1 = anno % 100
division2 = anno % 4
if division == 0:
    print("El anno", anno, "un año bisiesto")
elif division1 == 0:
    print("El anno", anno, "no es un anno bisiesto")
elif division2 == 0:
    print("El anno", anno, "un año bisiesto")
else:
    print("El anno", anno, "no es un anno bisiesto")