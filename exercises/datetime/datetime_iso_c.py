"""
* Assignment: Datetime ISO List
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Use list comprehension and `datetime.fromisoformat()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Skorzystaj z rozwinięcia listowego oraz `datetime.fromisoformat()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `[x for x in DATA]`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> result = list(result)

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'

    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> pprint(result, width=30)
    [datetime.datetime(1961, 4, 12, 6, 7),
     datetime.datetime(1961, 4, 12, 6, 7)]
"""

from datetime import datetime

DATA = [
    '1961-04-12 06:07',
    '1961-04-12 06:07:00',
]

# parsed DATA
# type: list[datetime]
result = [datetime.fromisoformat(date) for date in DATA]

