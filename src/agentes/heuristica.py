def sudokuHeuristic(state, problem):
    """
    Heurística para Sudoku basada en:
    1. Número de celdas vacías restantes
    2. Restricciones de valores legales (MRV)
    3. Conflictos potenciales en filas/columnas/bloques
    """
    emptyCells = 0
    totalConst = 0
    
    for i in range(9):
        for j in range(9):
            if state[i][j] == 0:
                emptyCells += 1
                # Contar restricciones: valores legales disponibles
                legalVal = problem.getLegalValues(state, i, j)
                if len(legalVal) == 0:
                    return float('inf')  # Estado inválido
                totalConst += len(legalVal)
    
    # Heurística: celdas vacías + penalización por restricciones
    # Menos restricciones = más cerca de la solución
    if emptyCells == 0:
        return 0  
    
    constFactor = totalConst / (emptyCells * 9)
    
    return emptyCells + constFactor

def blankHeuristic(state, problem):
    emptyCells = 0
    for i in range(9):
        for j in range(9):
            if state[i][j] == 0:
                emptyCells += 1
    return emptyCells