dia = int(input("Digite el dia de su cumpleaños"))
mes = int(input("Digite el mes de su cumpleaños"))
anno = int(input("Digite el anno de su cumpleaños"))
dia1 = int(input("Digite que dia es hoy"))
mes1 = int(input("Digite el mes de hoy"))
anno1 = int(input("Digite el anno en el que esta actualmente"))
resultado = anno1 - anno
if mes > mes1:
    casos = resultado - 1
    print("Usted tiene", casos, "annos")
else:
    print("Usted tiene", resultado, "annos")