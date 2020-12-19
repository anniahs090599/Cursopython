renta=float(input('Ingrese su renta: '))

if renta<10000:
    impuesto=5
elif renta>10000 or renta<20000:
    impuesto=15
elif renta>20000 or renta<35000:
    impuesto=20
elif renta>35000 or renta<60000:
    impuesto=45
elif renta>60000:
    impuesto=30
print('tu impuesto es '+str(impuesto)+'%')