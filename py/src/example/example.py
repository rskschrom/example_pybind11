from ._example import add as _add

def add(i, j):
    '''
    A wrapper function to _add that adds to integers.
    
    Parameters
    ----------
    i : int
        The first integer.
    j : int
        The second integer.
        
    Returns
    -------
    int
        The sum of `i` and `j`.
    '''
    return _add(i, j)
