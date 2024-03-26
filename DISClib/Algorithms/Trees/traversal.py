

import config
from DISClib.ADT import list as lt
assert config


def inorder(omap):
    """
    Implementa un recorrido inorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = inorderTree(omap['root'], lst)
    return lst


def preorder(omap):
    """
    Implementa un recorrido preorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = preorderTree(omap['root'], lst)
    return lst


def postorder(omap):
    """
    Implementa un recorrido postorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = postorderTree(omap['root'], lst)
    return lst


# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________


def inorderTree(root, lst):
    if (root is None):
        return None
    else:
        inorderTree(root['left'], lst)
        lt.addLast(lst, root['value'])
        inorderTree(root['right'], lst)
    return lst


def postorderTree(root, lst):
    if (root is None):
        return None
    else:
        postorderTree(root['left'], lst)
        postorderTree(root['right'], lst)
        lt.addLast(lst, root['value'])
    return lst


def preorderTree(root, lst):
    if (root is None):
        return None
    else:
        lt.addLast(lst, root['value'])
        preorderTree(root['left'], lst)
        preorderTree(root['right'], lst)
    return lst
