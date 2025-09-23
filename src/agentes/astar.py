from ..utils import PriorityQueue, state2Tuple, tuple2State

def aStarSearch(problem, heuristic):
    frontera = PriorityQueue()
    visitados = set()
    padres = {}
    acciones = {}
    costos = {} 

    estadoInicial = problem.getInitialState()
    estadoInicialT = state2Tuple(estadoInicial)
    frontera.push(estadoInicialT, heuristic(estadoInicial,problem))
    padres[estadoInicialT] = None
    acciones[estadoInicialT] = []
    costos[estadoInicialT] = 0
    
    while frontera.isEmpty()!=True:
        nodoT = frontera.pop()
        if nodoT in visitados:
            continue
        visitados.add(nodoT)
        
        nodo = tuple2State(nodoT)
        
        if problem.isGoalState(nodo):
            return acciones[nodoT]
        
        sucesores = problem.getSuccessors(nodo)
        for sucesor, accion, costo in sucesores:
            sucesorT = state2Tuple(sucesor)
            if sucesorT not in visitados:
                costoTotal = costos[nodoT] + costo
                if (sucesorT not in costos) or (costoTotal < costos[sucesorT]):
                    frontera.push(sucesorT, costoTotal + heuristic(sucesor,problem))
                    padres[sucesorT] = nodoT
                    acciones[sucesorT] = acciones[nodoT] + [accion]
                    costos[sucesorT] = costoTotal
    return []