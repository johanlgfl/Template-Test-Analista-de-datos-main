

import config
from DISClib.Utils import error as error
from DISClib.ADT import list as lt
assert config


"""
  Este módulo implementa el tipo abstracto de datos
  cola (Queue) sobre una lista.
"""


def newQueue(datastructure='SINGLE_LINKED'):
    """ Crea una cola vacia basada en una lista.
    Args:
        datastructure:  Indica el tipo de estructura de datos a utilizar
                        para implementar la cola
    Returns:
        Una cola vacia
    Raises:
        Exception
    """
    try:
        return lt.newList(datastructure)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->newQueue: ')


def enqueue(queue, element):
    """Agrega el elemento element en el tope de la pila
    Args:
        queue: La cola donde se insertará el elemento
        element:  El elemento a insertar

    Returns:
        La cola modificada
    Raises:
        Exception
    """
    try:
        lt.addLast(queue, element)
        return queue
    except Exception as ex:
        error.reraise(ex, 'enqueue ')


def dequeue(queue):
    """ Retorna el elemento en la primer posición de la cola, y lo elimina.
     Args:
        queue: La cola donde se eliminará el elemento

    Returns:
        El primer elemento de la cola
    Raises:
        Exception
    """
    try:
        return lt.removeFirst(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->dequeue: ')


def peek(queue):
    """ Retorna el elemento en la primer posición de la cola sin eliminarlo
    Args:
        queue: La cola  a examinar

    Returns:
        True el primer elemento de cola sin eliminarlo
    Raises:
        Exception
    """
    try:
        return lt.firstElement(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->isEmpty: ')


def isEmpty(queue):
    """Informa si la cola es vacía o no
    Args:
        queue: La cola  a examinar

    Returns:
        True si la cola es vacia, False de lo contrario
    Raises:
        Exception
    """
    try:
        return lt.isEmpty(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->isEmpty: ')


def size(queue):
    """Informa el número de elementos en la cola
    Args:
        queue: La cola  a examinar

    Returns:
        Retorna el tamaño de la cola

    Raises:
        Exception
    """
    try:
        return lt.size(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->size: ')
