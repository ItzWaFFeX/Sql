import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

print("Connection Successful")

import pandas as pd

tables = pd.read_sql(
    """SELECT  *
    FROM sqlite_master
    WHERE type='table';
""", conn)

matches = pd.read_sql(
    """SELECT *
        FROM Match;
    """, conn)

teams = pd.read_sql(
    """SELECT *
    FROM Team;
""",conn)



print(teams)














9
