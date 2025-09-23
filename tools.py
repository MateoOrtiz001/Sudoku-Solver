def imprimir_sudoku(sudoku):
    """Imprime el sudoku de forma legible"""
    for i, fila in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, valor in enumerate(fila):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(valor if valor != 0 else ".", end=" ")
        print()

def aplicar_acciones(estado_inicial, acciones):
    """Aplica las acciones para obtener el estado final"""
    estado = [fila[:] for fila in estado_inicial]  # Clonar
    for i, j, valor in acciones:
        estado[i][j] = valor
    return estado

def transformar_tablero(sudoku):
    """Formateamos los tableros producidos aleatoriamente por la libreria Sudoku"""
    sT = sudoku
    for i in range(9):
        for j in range(9):
            if sT[i][j] == None:
                sT[i][j] = 0
    return sT