"""
* Assignment: JSON Encoder Function
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define `result: str` with JSON encoded `DATA`
    2. Use encoder function
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z zakodowanym `DATA` w JSON
    2. Użyj enkodera funkcyjnego
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert isfunction(encoder), \
    'Encoder must be a function'

    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    {"mission": "Ares 3",
     "launch_date": "2035-06-29T00:00:00",
     "destination": "Mars",
     "destination_landing": "2035-11-07T00:00:00",
     "destination_location": "Acidalia Planitia",
     "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"},
              {"name": "Rick Martinez", "born": "1996-01-21"},
              {"name": "Alex Vogel", "born": "1994-11-15"},
              {"name": "Chris Beck", "born": "1999-08-02"},
              {"name": "Beth Johanssen", "born": "2006-05-09"},
              {"name": "Mark Watney", "born": "1994-10-12"}]}
"""

import json
from datetime import date, datetime
from typing import Any


DATA = {
    'mission': 'Ares 3',
    'launch_date': datetime(2035, 6, 29),
    'destination': 'Mars',
    'destination_landing': datetime(2035, 11, 7),
    'destination_location': 'Acidalia Planitia',
    'crew': [
        {'name': 'Melissa Lewis', 'born': date(1995, 7, 15)},
        {'name': 'Rick Martinez', 'born': date(1996, 1, 21)},
        {'name': 'Alex Vogel', 'born': date(1994, 11, 15)},
        {'name': 'Chris Beck', 'born': date(1999, 8, 2)},
        {'name': 'Beth Johanssen', 'born': date(2006, 5, 9)},
        {'name': 'Mark Watney', 'born': date(1994, 10, 12)}]}


# JSON encoder
def encoder(value: Any) -> str:
    if isinstance(value, date | datetime):
        return value.isoformat()


# JSON encoded DATA
# type: str
result = json.dumps(DATA, default=encoder)


