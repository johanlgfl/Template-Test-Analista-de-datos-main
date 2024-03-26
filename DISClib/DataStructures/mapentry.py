


def newMapEntry(key, value):
    """
    Retorna una pareja llave valor para ser guardada
    en un Map
    Args:
        key: llave
        value: valor
    Returns:
        una entrada con la pareja llave-valor
    Raises:
        Exception
    """
    entry = {'key': key, 'value': value}
    return entry


def setKey(entry, key):
    """
    Asigna una llave a una pareja de un Map
    Args:
        entry: la pareja llave valor
        key: la nueva llave
    Returns:
        La pareja modificada
    Raises:
        Exception
    """
    entry['key'] = key
    return entry


def setValue(entry, value):
    """
    Asigna un nuevo valor a una pareja de un Map
    Args:
        entry: la pareja llave valor
        value: el nuevo valor
    Returns:
        La pareja modificada
    Raises:
        Exception
    """
    entry['value'] = value
    return entry


def getKey(entry):
    """
    Retorna la llave de una pareja de un Map
    Args:
        entry: la pareja llave valor
    Returns:
        La llave de la pareja
    Raises:
        Exception
    """
    return entry['key']


def getValue(entry):
    """
    Retorna el valor de una pareja de un Map
    Args:
        entry: la pareja llave valor
    Returns:
        La llave de la pareja
    Raises:
        Exception
    """
    return entry['value']
