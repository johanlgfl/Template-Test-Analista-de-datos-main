

RED = 0
BLACK = 1


def newNode(key, value, size, color):
    """
    Crea un nuevo nodo para un árbol rojo-negro  y lo retorna.
    color:0 - rojo  color:1 - negro
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo
        color: El color inicial del nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    node = {'key': key,
            'value': value,
            'size': size,
            'parent': None,
            'left': None,
            'right': None,
            'color': color,
            'type': 'RBT'}

    return node


def isRed(node):
    """
    Informa si un nodo es rojo
    Args:
        node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Exception
    """
    return (node['color'] == RED)


def getValue(node):
    """ Retorna el valor asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['value'])
    return node


def getKey(node):
    """ Retorna la llave asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['key'])
    return node

