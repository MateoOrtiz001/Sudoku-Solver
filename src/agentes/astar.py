import utils
def aStarSearch(problem, heuristic):
    frontera = utils.PriorityQueue()
    visitados = set()
    padres = {}
    acciones = {}
    costos = {} 

    estadoInicial = problem.getStartState()
    frontera.push(estadoInicial, heuristic(estadoInicial,problem))
    padres[estadoInicial] = None
    acciones[estadoInicial] = []
    costos[estadoInicial] = 0
    
    while frontera.isEmpty()!=True:
        nodo = frontera.pop()
        if nodo in visitados:
            continue
        visitados.add(nodo)
        if problem.isGoalState(nodo):
            return acciones[nodo]
        sucesores = problem.getSuccessors(nodo)
        for sucesor, accion, costo in sucesores:
            if sucesor not in visitados:
                costoTotal = costos[nodo] + costo
                if (sucesor not in costos) or (costoTotal < costos[sucesor]):
                    frontera.push(sucesor, costoTotal + heuristic(sucesor,problem))
                    padres[sucesor] = nodo
                    acciones[sucesor] = acciones[nodo] + [accion]
                    costos[sucesor] = costoTotal
    return []