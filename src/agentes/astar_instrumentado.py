from utils import PriorityQueue, state2Tuple, tuple2State

def aStarSearchInstrumentado(problem, heuristic):
    """
    Versión instrumentada de A* que registra estadísticas del espacio de estados explorado
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
    estadoInicial_tuple = state2Tuple(estadoInicial)
    frontera.push(estadoInicial_tuple, heuristic(estadoInicial,problem))
    padres[estadoInicial_tuple] = None
    acciones[estadoInicial_tuple] = []
    costos[estadoInicial_tuple] = 0
    stats['nodos_generados'] = 1
    
    while frontera.isEmpty()!=True:
        # Actualizar máximo de nodos en frontera
        if len(frontera.heap) > stats['nodos_en_frontera_max']:
            stats['nodos_en_frontera_max'] = len(frontera.heap)
            
        nodo_tuple = frontera.pop()
        if nodo_tuple in visitados:
            continue
        visitados.add(nodo_tuple)
        stats['nodos_expandidos'] += 1
        
        # Convertir nodo de vuelta a lista para las operaciones del problema
        nodo = tuple2State(nodo_tuple)
        
        # Calcular profundidad actual
        profundidad_actual = len(acciones[nodo_tuple])
        if profundidad_actual > stats['profundidad_maxima']:
            stats['profundidad_maxima'] = profundidad_actual
        
        if problem.isGoalState(nodo):
            stats['costo_solucion'] = costos[nodo_tuple]
            stats['tiempo_fin'] = time.time()
            return acciones[nodo_tuple], stats
        
        sucesores = problem.getSuccessors(nodo)
        for sucesor, accion, costo in sucesores:
            sucesor_tuple = state2Tuple(sucesor)
            stats['nodos_generados'] += 1
            
            if sucesor_tuple not in visitados:
                costoTotal = costos[nodo_tuple] + costo
                if (sucesor_tuple not in costos) or (costoTotal < costos[sucesor_tuple]):
                    frontera.push(sucesor_tuple, costoTotal + heuristic(sucesor,problem))
                    padres[sucesor_tuple] = nodo_tuple
                    acciones[sucesor_tuple] = acciones[nodo_tuple] + [accion]
                    costos[sucesor_tuple] = costoTotal
    
    stats['tiempo_fin'] = time.time()
    return [], stats
