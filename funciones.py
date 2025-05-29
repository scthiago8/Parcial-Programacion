def cargar_matriz_notas(n, m):
    """
    Solicito al usuario ingresar las notas de n alumnos en m exámenes y 
    Valido que las notas sean enteros entre 1 y 10.
        n : Cantidad de alumnos.
        m : Cantidad de exámenes por alumno.
   y retorna: Matriz con las notas de cada alumno.
    """
    matriz = []  # guarda las notas

    for i in range(n):  # Iteramos sobre la cantidad de alumnos
        fila = []  # creo una lista temporarl para guardar las notas del alumno
        print(f"Alumno {i + 1}")  # muestro en que alumno esta

        for j in range(m):  # Iteramos sobre la cantidad de exámenes
            nota_valida = False  # creo una bandera para repetir hasta ingresar una nota válida

            while not nota_valida:
                nota = input(f"Ingrese la nota del examen {j + 1} (1-10): ")
                
                if nota.isdigit():  # Verifico que sea un número entero
                    nota = int(nota)  # lo convierto a entero
                    
                    if 1 <= nota <= 10:  # Valido que esté en el rango permitido
                        fila.append(nota)  # si esta agrego la nota a la fila
                        nota_valida = True  # marco como valida para salir
                    else:
                        print("La nota debe estar entre 1 y 10.")  # Si no está en rango, muestra error
                else:
                    print("Debe ingresar un número entero.")  # Si no es número, muestra error

        matriz.append(fila)  # Guardo la fila de notas del alumno en la matriz

    return matriz  # Devuelvo la matriz completa


def porcentaje_aprobados(matriz):
    """
    Calcula y muestra el porcentaje de exámenes aprobados (nota >= 6)
    para cada alumno de la matriz de notas.

        matriz : Matriz con notas de alumnos.
    
    No retorna nada (muestra los resultados).
    """
    n = len(matriz)  # la Cantidad de alumnos
    m = len(matriz[0])  # la Cantidad de exámenes por alumno

    for i in range(n):  # Iteramos sobre cada alumno
        aprobados = 0  # Contador para notas mayores o iguales a 6

        for j in range(m):  # Iteramos sobre cada nota del alumno
            if matriz[i][j] >= 6:  # Si la nota es >= 6 esta aprobada
                aprobados += 1  # incremento el contador

        # Calculo el porcentaje de exámenes aprobados como número entero
        porcentaje = (aprobados * 100) // m
        print(f"Alumno {i + 1}: {porcentaje}% de exámenes aprobados")  # Mostramos el resultado