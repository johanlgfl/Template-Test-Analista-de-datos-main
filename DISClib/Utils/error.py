

def reraise(excp, *args):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    excp.args = args + excp.args
    raise excp.with_traceback(excp.__traceback__)
