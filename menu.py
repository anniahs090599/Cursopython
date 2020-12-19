n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0

print("""
1) Sumar los dos números
2) Restar los dos números
3) Multiplicar los dos números
""")

opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opcion == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")