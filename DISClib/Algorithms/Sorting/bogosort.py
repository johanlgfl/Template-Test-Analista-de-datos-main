

import config as cf
import random
from DISClib.ADT import list as lt
assert cf


def sort(lst, sort_crit):
    """sort ordena una lista de elementos utilizando el algoritmo de
    ordenamiento al azar (bogosort).

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.

    Returns:
        list: La lista ordenada.
    """
    size = lt.size(lst)
    while is_sorted(lst, sort_crit, size) is not True:
        lst = bogotsort(lst, size)
    return lst


def bogotsort(lst, size):
    """bogotsort reordena aleatoriamente los elementos de una lista.

    Args:
        lst (list): La lista a ordenar.
        size (int): tamaño de la lista.

    Returns:
        list: la lista reordenada aleatoriamente.
    """
    for pos in range(1, size):
        random_pos = random.randint(1, size)
        lt.exchange(lst, pos, random_pos)
    return lst


def is_sorted(lst, sort_crit, size):
    """is_sorted revisa elementos adyacentes en una lista para verificar si
    están ordenados.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.
        size (int): tamaño de la lista.

    Returns:
        bool: True si la lista está ordenada, False en caso contrario.
    """
    for pos in range(1, size):
        if sort_crit(lt.getElement(lst, pos),
                     lt.getElement(lst, pos + 1)) is not True:
            return False
    return True
