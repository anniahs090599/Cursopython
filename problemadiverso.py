def estudiante(n):
    notas=[]
    nombre=[]
    promedio=[]
    mensaje = []

    for i in range(n):
        name= input(f'Ingrese su nombre {i+1}: ')
        nombre.append(name)
        nota1 = int(input('Ingrese Nota 1: '))
        nota2 = int(input('Ingrese Nota 2: '))
        nota3 = int(input('Ingrese Nota 3: '))
        prom= int((nota1+nota2+nota3)/3)
        if prom > 3:
            mens='Aprobado'
            mensaje.append([mens])
        else:
            mens= 'Desaprobado'
            mensaje.append([mens])
       
        promedio.append([prom])
        notas.append([nota1,nota2,nota3])  

    print("Alumno \t \t Promedio \t \t Estado")
    for i in range(n):
        print(nombre[i],"\t \t", promedio[i],"\t \t", mensaje[i])
n=int(input("Digite la  cantidad de alumnos: "))
estudiante(n)