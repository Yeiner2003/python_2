
print("Bienvenido al calculador de nota definitiva")

nombre_estudiante = input("Ingrese el nombre del estudiante: ")

asignatura = input("Ingrese el nombre de la asignatura: ")

nota_parcial1 = float(input("Ingrese la nota del primer parcial (25%): "))

nota_parcial2 = float(input("Ingrese la nota del segundo parcial (20%): "))

nota_final = nota_parcial1 * 0.25 + nota_parcial2 * 0.20

if nota_final > 5.0:

    nota_final = 5.0
    
nota_parcial_final = float(input("Ingrese la nota del parcial final (55%): "))

nota_final += nota_parcial_final * 0.55

if nota_final > 5.0:

    nota_final = 5.0

print(f"La nota final de",nombre_estudiante, "en la asignatura de",asignatura, "es:" ,nota_final)




