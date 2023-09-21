"""
* Assignment: Datetime Timedelta Dict
* Complexity: easy
* Lines of code: 13 lines
* Time: 5 min

English:
    1. `DATA` is the time between Gagarin launch and Armstrong
       first step on the Moon
    2. Assume:
        a. year = 365.25 days
        b. month = 30.4375 days
    3. Define `result: dict[str, int]` representing period
    4. Run doctests - all must succeed

Polish:
    1. `DATA`, to czas który upłynął między startem Gagarina
       a pierwszym krokiem Armstronga na Księżycu
    2. Uwzględnij założenie:
        a. rok = 365.25 dni
        b. miesiąc = 30.4375 dni
    3. Zdefiniuj `result: dict[str, int]` reprezentujący okres
    4. Uruchom doctesty - wszystkie muszą się powieść

Given:
    * 8 years
    * 3 months
    * 8 days
    * 20 hours
    * 49 minutes
    * 15 seconds

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, must be a dict'

    >>> result.keys()
    dict_keys(['years', 'months', 'days', 'hours', 'minutes', 'seconds'])

    >>> assert all(type(value) is int for value in result.values()), \
    'All elements in `result` must be an int'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'years': 8,
     'months': 3,
     'days': 8,
     'hours': 20,
     'minutes': 49,
     'seconds': 15}
"""

from datetime import timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.4375 * DAY
YEAR = 365.25 * DAY

DATA = timedelta(days=3021, seconds=74955)

years, seconds = divmod(DATA.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(DATA.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

# dict[str, int]
result = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

