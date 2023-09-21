"""
* Assignment: RE Search Time
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use regular expressions to check `TEXT` [1]
       contains time in UTC (24 hour clock compliant with ISO-8601)
    2. Define `result: str` with matched time
    3. Use simplified checking `xx:xx UTC`,
       where `x` is a digit
    4. Text does not contain any invalid date
    5. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych do sprawdzenia czy `TEXT` [1]
       zawiera godzinę w UTC (format 24 godzinny zgodny z ISO-8601)
    2. Zdefiniuj `result: str` ze znalezionym czasem
    3. Użyj uproszczonego sprawdzania: `xx:xx UTC`,
       gdzie `x` to dowolna cyfra
    4. Tekst nie zawiera żadnej niepoprawnej godziny
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Hints:
    * `re.Match.group()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, 'result must be a str'
    >>> assert result.endswith('UTC'), 'result must contain timezone'

    >>> result
    '20:17 UTC'
"""

import re


TEXT = ("Apollo 11 was the spaceflight that first landed humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed "
        "the American crew that landed the Apollo Lunar Module Eagle on July "
        "20, 1969, at 20:17 UTC. Armstrong became the first person to step "
        "onto the lunar surface six hours and 39 minutes later on July 21 at "
        "02:56 UTC; Aldrin joined him 19 minutes later. They spent about two "
        "and a quarter hours together outside the spacecraft, and they "
        "collected 47.5 pounds (21.5 kg) of lunar material to bring back to "
        "Earth. Command module pilot Michael Collins flew the command module "
        "Columbia alone in lunar orbit while they were on the Moon's surface."
        "Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface"
        "at a site they named Tranquility Base before lifting off to rejoin "
        "Columbia in lunar orbit.")


# Pattern for searching time with timezone in 24 format, i.e. '23:59 UTC'
# Text does not contain any invalid date
# type: str
pattern = r'\d\d:\d\d [A-Z]+'

# use re.search() to find pattern in TEXT, get result text
# use .group() to get the value from re.Match object
# type: str
result = re.search(pattern, TEXT).group()


