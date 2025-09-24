#DOCS: https://docs.python.org/3/library/sqlite3.html

import sqlite3
con = sqlite3.connect("example.db") #establish connection to a databse

#to execute SQL queries we will need a "cursor"
cur = con.cursor()

#creates a new table
cur.execute("CREATE TABLE pet(name, type, age, is_alive)")

#get table names on the database
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone()) #print the first row

#if a query would return nothing it's value is None
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

#Insert several entries into the pet table
cur.execute("""
    INSERT INTO pet VALUES
        ('Monty', 'guniea pig', 85, True),
        ('Fern', 'rabbit', 2, True)
""") #indentation is for readablity.
#commit (save) the INSERT transaction
con.commit()

#We can select all the information of all entries on the pet table
# the * character represents all columns
res = cur.execute("select * from pet")
print(res.fetchall())


data = [
    ("James", "cat", 5, True),
    ("Ottis", "dog", 20, False),
    ("Camel", "camel", 97, False)
]
cur.executemany("INSERT INTO move VALUES(?, ?, ?)", data)

#sequentially print out all the data in the table:
for row in cur.execute("SELECT name, age FROM pet ORDER BY age"):
    print(row)