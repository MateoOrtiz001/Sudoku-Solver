def state2Tuple(state):
    """Convierte un estado (lista de listas) a tupla para hacerlo hashable"""
    return tuple(tuple(fila) for fila in state)

def tuple2State(state_tuple):
    """Convierte una tupla de estado de vuelta a lista de listas"""
    return [list(fila) for fila in state_tuple]
