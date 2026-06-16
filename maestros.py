salario = 4000  # Salario base

nombre = "Habram"

puntuacion = float(input("Ingrese la puntuación (0.0, 0.4 o 0.6): "))

if puntuacion == 0.0:
    nivel = "Inalcanzable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion == 0.6:
    nivel = "Meritorio"
else:
    print("Puntuación no válida.")
    exit()

beneficio = salario * puntuacion

print("\n--- Resultado de la evaluación ---")
print("Nombre del maestro:", nombre)
print("Nivel obtenido:", nivel)
print("Dinero que recibirá: $", beneficio)
