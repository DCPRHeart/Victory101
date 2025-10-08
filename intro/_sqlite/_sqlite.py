#DOCS: https://docs.python.org/3/library/sqlite3.html

import sqlite3
con = sqlite3.connect("example.db") #establish connection to a databse

#to execute SQL queries we will need a "cursor"
cur = con.cursor()

#creates a new table
cur.execute("""
    CREATE TABLE pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        age INTEGER,
        is_alive BOOLEAN
    )""")

#get table names on the database
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone()) #print the first row

#if a query would return nothing it's value is None
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")

#Insert several entries into the pet table
cur.execute("""
    INSERT INTO pet (name, type, age, is_alive) VALUES
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

# Add a new column to the pet table
cur.execute("ALTER TABLE pet ADD COLUMN owner TEXT")
con.commit()

# Update data in the table
cur.execute("UPDATE pet SET owner = 'Alice' WHERE name = 'Monty'")
cur.execute("UPDATE pet SET owner = 'Bob' WHERE name = 'Fern'")
con.commit()

# Delete a row from the table
cur.execute("DELETE FROM pet WHERE age > 20")
con.commit()

# Use parameterized queries to prevent SQL injection
pet_type = 'cat'
cur.execute("SELECT * FROM pet WHERE type = ?", (pet_type,))
print("Cats in the database:", cur.fetchall())

# Use transactions (rollback example)
try:
    cur.execute("INSERT INTO pet VALUES ('Test', 'test', 1, False)") #would still execute after rollback
    cur.execute("BEGIN")
    cur.execute("INSERT INTO pet VALUES ('Test', 'test', 1, 1, 'Tester')")
    #raise Exception("Simulated error")
    con.commit()
except Exception:
    con.rollback()
    con.commit()
    print("Transaction rolled back due to error.")

# Create an index to speed up queries
cur.execute("CREATE INDEX IF NOT EXISTS idx_pet_type ON pet(type)")
con.commit()

# Use aggregate functions
cur.execute("SELECT type, COUNT(*) FROM pet GROUP BY type")
print("Count of pets by type:", cur.fetchall())

#Ordered select by age
cur.execute("SELECT * FROM pet ORDER BY age ASC")

# Close the connection
con.close()