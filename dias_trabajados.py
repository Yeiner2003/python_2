def calcular_pagolaboral(dias_trabajados):
    valor_dia_trabajo = 136000
    pago_empleado = dias_trabajados * valor_dia_trabajo
    incentivo = 0

    
    if pago_empleado >= 1088000 and pago_empleado > 15:
       incentivo += 60000 

    if dias_trabajados >= 15:
        incentivo += 0.10 * pago_empleado


    if dias_trabajados >= 30:
       incentivo += 0.20 * pago_empleado

    pago_empleado = pago_empleado + incentivo
    return pago_empleado, incentivo, pago_empleado

dias_trabajados = int(input("Ingrese la cantidad de días laborados:\n "))
pago_empleado,incentivo, salario_total = calcular_pagolaboral(dias_trabajados)

print(f"Salario: ${pago_empleado:f}")
print(f"incentivo de 10% o 20%: ${incentivo:f}")
print(f"pago total dias trabajados: ${pago_empleado:f}")