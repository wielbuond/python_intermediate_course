"""
* Assignment: Database Insert Tuple
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data:
       a. table: contacts
       b. data: `DATA: tuple`
       c. use: prepared statement (with `?`)
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane:
       a. tabela: contacts
       b. dane: `DATA: tuple`
       c. użyj: przygotowanego zapytania (z `?`)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:

"""

import sqlite3


# Write SQL query to insert data:
# - table: contacts
# - data: `DATA: tuple`
# - use: prepared statement (with `?`)
# type: str
result = """

INSERT INTO contacts (firstname, lastname)
VALUES ()

"""


DATA = ('Mark', 'Watney')

with sqlite3.connect('sql.db') as db:
    db.execute(result, DATA)
