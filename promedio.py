nota1 = float(input("Ingrese la primera nota "))
nota2 = float(input("Ingrese la segunda nota "))
nota3 = float(input("Ingrese la tercera nota "))

resultado = (nota1+nota2+nota3)/3
if resultado >= 4:
    print(f'El promedio es de {resultado}, usted está aprovado.')
else:
    print("Usted no tiene el promedio suficiente para aprovar.")