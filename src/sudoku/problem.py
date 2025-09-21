class SudokuProblem:
    def __init__(self, heuristic, startState=None):
        self.heuristic = heuristic
        self.startState = startState
        
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
            
        for bloque_fila in range(3):
            for bloque_col in range(3):
                bloque = []
                for i in range(3):
                    for j in range(3):
                        fila = bloque_fila * 3 + i
                        col = bloque_col * 3 + j
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
    
    
    def getSucessors(self, state):
        sucessors = []
        
        return 0

    def getCostos(self, actions):
        # Implement A* pathfinding algorithm here
        pass