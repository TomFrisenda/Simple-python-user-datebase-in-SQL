#Author: Tom Frisenda
#Purpose: Frame work for creating and querying and SQLite DB in python

import bcrypt,random,sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("""CREATE TABLE db (
            username TEXT,
            hash TEXT,
            salt TEXT,
            personalInfo TEXT
            )""")
conn.commit()
s = bcrypt.gensalt()

def registration(s):
    u = input("enter unique id (Username):")
    p = input("enter password:").encode()
    PI = input("enter profile information:")
    h = bcrypt.hashpw(p,s)
    c.execute("INSERT INTO login (username, hash, salt, personalInfo) VALUES (?, ?, ?, ?)", (u, h, s, PI))
    conn.commit()
    return s


def login(s):

    un =str(input("enter unique id (Username):"))
    p2 = input("enter password:").encode()
    loginhash = bcrypt.hashpw(p2,s)
    c.execute("SELECT hash FROM login WHERE username == (?);",(un,))
    h = c.fetchone()
    if loginhash in h:
        print("password match")
    else:
        print("password no match")

registration(s)
login(s)
