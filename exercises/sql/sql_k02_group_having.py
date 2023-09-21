"""
* Assignment: Database Group Having
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: apollo11
       b. column: category
       c. what: unique category names
       d. where: category is has less than 50 occurrences
       e. use: GROUP BY and HAVING
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: apollo11
       b. kolumna: category
       c. jakie: unikalne nazwy kategorii
       d. gdzie: kategoria ma mniej niż 50 wystąpień
       e. użyj: GROUP BY oraz HAVING
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:

"""

import sqlite3


# Write SQL query to select data:
# - table: apollo11
# - column: category
# - what: unique category names
# - where: category is has less than 50 occurrences
# - use: GROUP BY and HAVING
result = """

SELECT category
FROM apollo11
GROUP BY category

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(result)):
        print(result)
