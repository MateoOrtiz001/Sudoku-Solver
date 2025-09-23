from utils import PriorityQueue, state2Tuple, tuple2State

def uniformCostSearchInstrumentado(problem):
    """
    Versión instrumentada de Costo Uniforme que registra estadísticas del espacio de estados explorado
    """
    frontera = PriorityQueue()
    visitados = set()
    padres = {}
    acciones = {}
    costos = {} 
    
    # Estadísticas de exploración
    stats = {
        'nodos_expandidos': 0,
        'nodos_generados': 0,
        'nodos_en_frontera_max': 0,
        'profundidad_maxima': 0,
        'costo_solucion': 0,
        'tiempo_inicio': None,
        'tiempo_fin': None
    }
    
    import time
    stats['tiempo_inicio'] = time.time()

    estadoInicial = problem.getInitialState()
    estadoInicialT = state2Tuple(estadoInicial)
    frontera.push(estadoInicialT, 0)
    padres[estadoInicialT] = None
    acciones[estadoInicialT] = []
    costos[estadoInicialT] = 0 
    stats['nodos_generados'] = 1
    
    while frontera.isEmpty()!=True:
        # Actualizar máximo de nodos en frontera
        if len(frontera.heap) > stats['nodos_en_frontera_max']:
            stats['nodos_en_frontera_max'] = len(frontera.heap)
            
        nodoT = frontera.pop()
        if nodoT in visitados:
            continue
        visitados.add(nodoT)
        stats['nodos_expandidos'] += 1
        
        nodo = tuple2State(nodoT)
        
        # Calcular profundidad actual
        profundidad_actual = len(acciones[nodoT])
        if profundidad_actual > stats['profundidad_maxima']:
            stats['profundidad_maxima'] = profundidad_actual
        
        if problem.isGoalState(nodo):
            stats['costo_solucion'] = costos[nodoT]
            stats['tiempo_fin'] = time.time()
            return acciones[nodoT], stats
        
        sucesores = problem.getSuccessors(nodo)
        for sucesor, accion, costo in sucesores:
            sucesorT = state2Tuple(sucesor)
            stats['nodos_generados'] += 1
            
            if sucesorT not in visitados:
                costoTotal = costos[nodoT] + costo
                if (sucesorT not in costos) or (costoTotal < costos[sucesorT]):
                    frontera.push(sucesorT, costoTotal)
                    padres[sucesorT] = nodoT
                    acciones[sucesorT] = acciones[nodoT] + [accion]
                    costos[sucesorT] = costoTotal
    
    stats['tiempo_fin'] = time.time()
    return [], stats
