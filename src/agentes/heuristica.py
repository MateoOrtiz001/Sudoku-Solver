def sudokuHeuristic(state, problem):
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