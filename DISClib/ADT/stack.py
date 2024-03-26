

import config
from DISClib.Utils import error as error
from DISClib.ADT import list as lt
assert config

"""
  Este módulo implementa el tipo abstracto de datos pila
  (Stack) sobre una lista encadenada.
"""


def newStack(datastructure='DOUBLE_LINKED'):
    """ Crea una pila vacia.

    Args:
        datastructure:  Indica el tipo de estructura de datos a utilizar
                        para implementar la pila
    Returns:
        Una pila vacia
    Raises:
        Exception
    """
    try:
        return lt.newList(datastructure, None)
    except Exception as exp:
        error.reraise(exp, 'TADStack->newStack: ')


def push(stack, element):
    """ Agrega el elemento element en el tope de la pila.

    Args:
        stack:  La pila donde se insetará el elemento
        element:  El elemento a insertar

    Returns:
        La pila modificada

    Raises:
        Exception
    """
    try:
        lt.addLast(stack, element)
        return stack
    except Exception as exp:
        error.reraise(exp, 'TADStack->Push: ')


def pop(stack):
    """ Retorna el elemento  presente en el tope de la pila.

     Args:
        stack:  La pila de donde se retirara el elemento

    Returns:
        El elemento del tope de la pila

    Raises:
        Exception
    """
    try:
        if stack is not None and not lt.isEmpty(stack):
            return lt.removeLast(stack)
        else:
            raise Exception
    except Exception as exp:
        error.reraise(exp, 'TADStack->pop: ')


def isEmpty(stack):
    """Informa si la pila es vacía o no
     Args:
        stack:  La pila a examinar

    Returns:
        True si la pila es vacia
        False de lo contrario

    Raises:
        Exception
    """
    try:
        return lt.isEmpty(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->isEmpty: ')


def top(stack):
    """ Retorna el elemento en tope de la pila, sin eliminarlo de la pila

    Args:
        stack:  La pila a examinar

    Returns:
        El primer elemento de la pila, sin eliminarlo

    Raises:
        Exception
    """
    try:
        return lt.lastElement(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->top: ')


def size(stack):
    """ Informa el número de elementos en la pila
    Args:
        stack: La pila a examinar

    Returns:
        Retorna el tamaño de la pila

    Raises:
        Exception
    """
    try:
        return lt.size(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->size: ')
