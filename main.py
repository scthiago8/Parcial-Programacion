
from funciones import cargar_matriz_notas, porcentaje_aprobados  # Importo las funciones 

# Solicito la cantidad de alumnos y exámenes al usuario
n = int(input("Ingrese la cantidad de alumnos: "))  # cantidad de alumnos
m = int(input("Ingrese la cantidad de exámenes: "))  # cantidad de exámenes

# Carga las notas y guarda el resultado en una matruz
matriz = cargar_matriz_notas(n, m)

# Muestra el porcentaje de exámenes aprobados por cada alumno
porcentaje_aprobados(matriz)
