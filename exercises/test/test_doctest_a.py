"""
* Assignment: Test Doctest Distance
* Required: no
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    1. Write doctests to a functions which convert distance given in kilometers to meters
    2. Valid arguments:
        a. `int`
        b. `float`
    3. Invalid argumentm, raise exception `TypeError`:
        a. `str`
        b. `list[int]`
        c. `list[float]`
        d. `bool`
        e. any other type
    4. Returned distance must be float
    5. Returned distance cannot be negative
    6. Run doctests - all must succeed

Polish:
    1. Napisz doctesty do funkcji, która przeliczy dystans podany w kilometrach na metry
    2. Poprawne argumenty:
        a. `int`
        b. `float`
    3. Niepoprawne argumenty, podnieś wyjątek `TypeError`:
        a. `str`
        b. `list[int]`
        c. `list[float]`
        d. `bool`
        e. any other type
    4. Zwracany dystans musi być float
    5. Zwracany dystans nie może być ujemny
    6. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * 1 km = 1000 m

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""

def km_to_meters(kilometers):
    if type(kilometers) not in {int, float}:
        raise TypeError('Invalid argument type')
    if kilometers < 0:
        raise ValueError('Argument must be not negative')
    return float(kilometers * 1000)


