

import config as cf
from DISClib.ADT import list as lt
assert cf

"""
Implementación del algoritmo shellsort, basado en
la propuesta de Robert Sedgewick

Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne

Se utiliza la secuencia de incrementos 3x+1: 1, 4, 13, 40, 121, 364, 1093,
(D. Knuth)
Sedgewick: 1,5,19,41,109,209,929,2161,...
"""


def sort(lst, sort_crit):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst
