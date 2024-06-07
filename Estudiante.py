# def calculo_nota_final(not1, not2, not3):
#     primer_par = 0.25
#     segundo_par = 0.25
#     parcial_final = 0.55

#     return not1 * primer_par + not2 * segundo_par + not3 * parcial_final

# def validar():
#  while True:
    
#     alumno = input("Ingresa tu nombre por favor:\n")
#     asignatura = input("Ingresa la asignatura por favor:\n")
#     cedula = input("Ingrese su numero de cedula por favor:\n")

  
#     not1 = float(input("Ingresa la nota del primer parcial por favor:\n"))
#     if not1 > 5.0:
#         print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
#         return

#     not2 = float(input("Ingresa la nota del segundo parcial por favor:\n"))
#     if not2 > 5.0:
#         print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
#         return

#     not3 = float(input("Ingresa la nota del parcial final por favor:\n"))
#     if not3 > 5.0:
#         print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
#         return

#     nota_final = calculo_nota_final(not1, not2, not3)
  
#     print("La nota final de %s en la asignatura %s es %.2f" % (alumno, asignatura, nota_final))
# # 2f permite que lea la nota del alumno en dos decimales obteniendo una representacion precisa 

# validar()


def calculo_nota_final(not1, not2, not3):
    primer_par = 0.25
    segundo_par = 0.25
    parcial_final = 0.55

    return not1 * primer_par + not2 * segundo_par + not3 * parcial_final

def validar():
    estudiantes = []  # Lista para almacenar los datos de los estudiantes
    while True:
        alumno = input("Ingresa tu nombre por favor (o escribe 'fin' para terminar):\n")
        if alumno.lower() == 'fin':
            break  # Termina el bucle si el usuario escribe 'fin'
        
        asignatura = input("Ingresa la asignatura por favor:\n")
        cedula = input("Ingrese su numero de cedula por favor:\n")

        not1 = float(input("Ingresa la nota del primer parcial por favor:\n"))
        if not1 > 5.0:
            print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
            continue  # Continúa con la siguiente iteración del bucle

        not2 = float(input("Ingresa la nota del segundo parcial por favor:\n"))
        if not2 > 5.0:
            print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
            continue

        not3 = float(input("Ingresa la nota del parcial final por favor:\n"))
        if not3 > 5.0:
            print("Calificación incorrecta. La nota debe ser menor o igual a 5.0.")
            continue

        nota_final = calculo_nota_final(not1, not2, not3)
        estudiantes.append((alumno, asignatura, nota_final))  # Agrega los datos del estudiante a la lista

    # Calcular el promedio de cada estudiante
    for estudiante in estudiantes:
        print("El promedio de %s en la asignatura %s es %.2f" % (estudiante[0], estudiante[1], estudiante[2]))

    # Identificar al estudiante con la mayor nota
    max_nota = max(estudiantes, key=lambda x: x[2])  # Encuentra el estudiante con la mayor nota
    print("El estudiante con la mayor nota es %s en la asignatura %s con una nota de %.2f" % (max_nota[0], max_nota[1], max_nota[2]))

validar()
