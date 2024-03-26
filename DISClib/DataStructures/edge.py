

import config
assert config

"""
Este código está basado en las implementaciones propuestas en:
- Algorithms, 4th Edition.  R. Sedgewick
- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""


def newEdge(va, vb, weight=0):
    """
    Crea un nuevo arco entrelos vertices va y vb
    """
    edge = {'vertexA': va,
            'vertexB': vb,
            'weight': weight
            }
    return edge


def weight(edge):
    """
    Retorna el peso de un arco
    """
    return edge['weight']


def either(edge):
    """
    Retorna el vertice A del arco
    """
    return edge['vertexA']


def other(edge, veither):
    """
    Retorna el vertice B del arco
    """
    if (veither == edge['vertexA']):
        return edge['vertexB']
    elif (veither == edge['vertexB']):
        return edge['vertexA']

def set_weight(edge, weight):
    """
    NEW FUNCTION
    actualizar el peso de un arco
    """
    edge['weight'] = weight

def compareedges(edge1, edge2):
    """
    Funcion utilizada en lista de edges para comparar dos edges
    Retorna 0 si los arcos son iguales, 1 si edge1 > edge2, -1 edge1 < edge2
    """
    e1v = either(edge1)
    e2v = either(edge2)

    if e1v == e2v:
        if other(edge1, e1v) == other(edge2, e2v):
            return 0
        elif other(edge1, e1v) > other(edge2, e2v):
            return 1
        else:
            return -1
    elif e1v > e2v:
        return 1
    else:
        return -1
