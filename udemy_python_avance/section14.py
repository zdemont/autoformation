"""
Module pour realiser des operations mathematiques de base
tel que l'addition, la multiplication ou la soustraction
"""

def division(a, b):
    """Divise deux nombres et retourn le resultat de l'operation

    Args:
        a (int): Le premier nombre
        b (int): Le deuxieme nombre

    Returns:
        int: Le resultat de la division


    Exemple:
    >>> division(10, 5)
    2

    """
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division par 0 impossible...'
    except TypeError:
        return 'Svp, entrez deux nombres entiers...'



def multiplication(a, b):
    """Multiplie deux nombres et retourne le resultat de l'operation

    :param a: Le premier nombre
    :param b: Le deuxieme nombre
    :type a: int
    :type b: int
    :return: Le resultat de la multiplication
    :rtype: int

    :Example:

    >>> multiplication(2, 5)
    10

    """
    return a * b

