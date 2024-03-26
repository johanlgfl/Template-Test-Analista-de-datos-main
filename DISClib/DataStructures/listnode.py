


def newSingleNode(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    node = {'info': element, 'next': None}
    return(node)


def getElement(node):
    """
    Retorna la información de un nodo
    Args:
      node: El nodo a examinar
    Returns:
      La información almacenada en el nodo
    """
    return node['info']


def newDoubleNode(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    doblemente
    """
    node = {'info': element,
            'next': None,
            'prev': None
            }
    return node
