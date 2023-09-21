"""
* Assignment: Datetime Parse US
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: datetime` with parsed date `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: datetime` ze sparsowaną datą `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 12-hour clock

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, must be a datetime'

    >>> result
    datetime.datetime(1969, 7, 21, 2, 56, 15)
"""

from datetime import datetime


DATA = 'July 21, 1969 2:56:15 AM'

# DATA from US long format
# type: datetime
result = datetime.strptime(DATA, '%B %d, %Y %I:%M:%S %p')

