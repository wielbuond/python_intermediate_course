"""
* Assignment: Database Create Table
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Write SQL query to create table:
       a. table: contacts
       b. column: id, integer, primary key, autoincrement
       c. column: firstname, text
       d. column: lastname, text
       e. column: birthday, date, default null
       f. use: IF NOT EXISTS
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć tabelę:
       a. tabela: contacts
       b. kolumna: id, integer, primary key, autoincrement
       c. kolumna: firstname, text
       d. kolumna: lastname, text
       e. kolumna: birthday, date, default null
       f. użyj: IF NOT EXISTS
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent / 'sql.db'

    >>> with sqlite3.connect(database) as db:
    ...     db.row_factory = sqlite3.Row
    ...     _ = db.execute(result)
    ...     sql = 'SELECT name FROM sqlite_master WHERE type="table"'
    ...     for table in db.execute(sql):
    ...         print(table['name'])
    apollo11
    addresses
    sqlite_sequence
    astronauts
    missions
    contacts


"""


# SQL query to create table:
# - table: contacts
# - column: id, integer, primary key, autoincrement
# - column: firstname, text
# - column: lastname, text
# - column: birthday, date, default null
# - use: IF NOT EXISTS
# type: str
result = """

-- replace this comment
-- with your sql query

"""
