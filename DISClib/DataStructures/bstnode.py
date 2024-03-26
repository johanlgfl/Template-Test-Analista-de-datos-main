

def newNode(key, value, size):
    """ Crea un nuevo nodo para un árbol binario y lo retorna
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    node = {'key': key,
            'value': value,
            'size': size,
            'left': None,
            'right': None,
            'type': 'BST'}
    return node


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
