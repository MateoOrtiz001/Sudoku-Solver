class SudokuProblem:
    def __init__(self, heuristic, startState=None):
        self.heuristic = heuristic
        self.startState = startState
        
    def getInitialState(self):
        return self.startState
    
    def isGoalState(self, state):
        for fila in state:
            for elemento in fila:
                if elemento == 0:
                    return False
                
        for fila in state:
            if not self.isValidState(fila):
                return False
            
        for col in range(9):
            columna = [state[fila][col] for fila in range(9)]
            if not self.isValidState(columna):
                return False
            
        for bloqueFila in range(3):
            for bloqueCol in range(3):
                bloque = []
                for i in range(3):
                    for j in range(3):
                        fila = bloqueFila * 3 + i
                        col = bloqueCol * 3 + j
                        bloque.append(state[fila][col])
                if not self.isValidState(bloque):
                    return False
        
        return True
    
    def isValidState(self, conjunto):
        numeros = [num for num in conjunto if num != 0]
        if len(numeros) != 9:
            return False
        for num in numeros:
            if num < 1 or num > 9:
                return False
        return len(set(numeros)) == 9
    
    
    def getSuccessors(self, state):
        successors = []

        minOp = 10
        target = None
        options = None

        for i in range(9):
            for j in range(9):
                if state[i][j] == 0:
                    # Valores posibles para esta celda
                    possible = self.getLegalValues(state, i, j)
                    if len(possible) < minOp:
                        minOp = len(possible)
                        target = (i, j)
                        options = possible

        if not target:
            return []  

        i, j = target
        for value in options:
            newState = [row[:] for row in state]
            newState[i][j] = value
            successors.append((newState, (i, j, value), 1))

        return successors

    def getLegalValues(self, state, row, col):
        if state[row][col] != 0:
            return []

        values = set(range(1, 10))
        values -= set(state[row])
        values -= {state[i][col] for i in range(9)}

        br, bc = 3 * (row // 3), 3 * (col // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                values.discard(state[i][j])

        return list(values)
