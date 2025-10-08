import sqlite3

con = sqlite3.connect("blog.db")
cur = con.cursor()
#initialize database
def __init__():
    
    cur.execute("""
    create table book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT)
    """)
    cur.execute("""
    create table review (
        id INTEGER PRIMARY KEY,
        title TEXT,
        plublish date DATE,
        body TEXT,
        book_id INTEGER,
        FORIEGN KEY (book_id) REFRENCES book (id)
    )
    """)
    con.commit()
    return

def add_book(title, author, genre):
    cur.execute("""
        INSERT INTO book (title, author, genre) VALUES
            (?, ?, ?) RETURNING id
    """, (title, author, genre))
    con.commit()
    return


def check_tables():
    cur.execute()


def drop_table(table_name):
    cur = con.cursor()
    cur.execute("drop table ?", (table_name))
    return
