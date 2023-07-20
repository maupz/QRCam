def solve_nanogram(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    solution = [[None] * cols for _ in range(rows)]  # Inicializar la solución vacía

    def backtrack(row, col):
        # Si hemos alcanzado la última columna, pasamos a la siguiente fila
        if col == cols:
            return backtrack(row + 1, 0)

        # Si hemos completado todas las filas, hemos encontrado una solución
        if row == rows:
            return True

        # Si la celda actual ya está llena, avanzamos a la siguiente celda
        if puzzle[row][col] == 1:
            solution[row][col] = 1
            return backtrack(row, col + 1)

        # Si la celda actual está vacía, intentamos llenarla y avanzar a la siguiente celda
        solution[row][col] = 0
        if is_valid(row, col) and backtrack(row, col + 1):
            return True

        # Si no es posible llenar la celda actual, probamos con el valor contrario
        solution[row][col] = 1
        if is_valid(row, col) and backtrack(row, col + 1):
            return True

        # Si ninguna de las opciones anteriores es válida, deshacemos la asignación y retrocedemos
        solution[row][col] = None
        return False

    def is_valid(row, col):
        # Comprueba si la asignación actual es válida según las restricciones de las pistas
        return check_row(row) and check_col(col)

    def check_row(row):
        # Comprueba si la fila cumple las restricciones de las pistas
        clues = puzzle[row]
        line = solution[row]
        return check_line(line, clues)

    def check_col(col):
        # Comprueba si la columna cumple las restricciones de las pistas
        clues = [puzzle[row][col] for row in range(rows)]
        line = [solution[row][col] for row in range(rows)]
        return check_line(line, clues)

    def check_line(line, clues):
        # Comprueba si una línea cumple las restricciones de las pistas
        groups = [list(run) for run, _ in groupby(line) if run]
        if len(groups) != len(clues):
            return False
        for group, clue in zip(groups, clues):
            if len(group) != clue:
                return False
        return True

    # Resuelve el nanograma comenzando desde la esquina superior izquierda (fila 0, columna 0)
    if backtrack(0, 0):
        return solution  # Devuelve la solución encontrada
    else:
        return None  # No se encontró ninguna solución

# Ejemplo de uso:
puzzle = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

solution = solve_nanogram(puzzle)
if solution:
    print("Solución encontrada:")
    for row in solution:
        print(row)
else:
    print("No se encontró solución.")

