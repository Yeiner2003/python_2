
def promedio(salarios):
    return sum(salarios) / len(salarios)

num_alumnos = int(input("Ingrese el número de alumnos: "))

carreras = {'administración': 0, 'derecho': 0, 'medicina': 0, 'sistemas': 0}

salarios_administracion = []

mujeres_sistemas = 0

total_sistemas = 0

edad_max_salario_medicina = 0

max_salario_medicina = 0

for i in range(num_alumnos):

    print(f"Ingrese los datos del alumno {i+1}:")

    while True:
        try:
            cedula = int(input("Cédula: "))
            break
        except ValueError:
            print("Error: Solo se pueden ingresar números para la cédula. Intente nuevamente.")

    nombre = input("Nombre: ")

    while True:
        try:
            salario = float(input("Salario: "))
            break
        except ValueError:
            print("Error: Solo se pueden ingresar números para el salario. Intente nuevamente.")

    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Error: Solo se pueden ingresar números para la edad. Intente nuevamente.")

    sexo = int(input("Sexo (1: femenino, 2: masculino): "))

    estado_civil = int(input("Estado civil (1: casado, 2: soltero, 3: divorciado): "))

    carrera = int(input("Carrera (1: administración, 2: derecho, 3: medicina, 4: sistemas): "))

    if carrera == 1:

        carreras['administración'] += 1

        if carrera == 1:

            salarios_administracion.append(salario)

    elif carrera == 2:

        carreras['derecho'] += 1

    elif carrera == 3:

        carreras['medicina'] += 1

        if salario > max_salario_medicina:

            max_salario_medicina = salario

            edad_max_salario_medicina = edad

    elif carrera == 4:

        carreras['sistemas'] += 1

        total_sistemas += 1

        if sexo == 1:

            mujeres_sistemas += 1

porcentaje_mujeres_sistemas = (mujeres_sistemas / total_sistemas) * 100 if total_sistemas > 0 else 0

carrera_max_alumnos = max(carreras, key=carreras.get)

promedio_salario_administracion = promedio(salarios_administracion) if len(salarios_administracion) > 0 else 0

print("\nResultados:")

print("Total de alumnos por carrera:", carreras)

print("Carrera con más alumnos:", carrera_max_alumnos)

print("Promedio de salario de los alumnos de administración:", promedio_salario_administracion)

print("Porcentaje de mujeres de sistemas:", porcentaje_mujeres_sistemas)

print("Edad de la persona con mayor salario en medicina:", edad_max_salario_medicina)


