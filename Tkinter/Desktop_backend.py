import sqlite3

def connect():
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS SHOP (id INTEGER PRIMARY KEY, product TEXT, profit INTEGER,loss INTEGER,client TEXT)")
    conn.commit()
    conn.close()


def insert(product,profit,loss,client):
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO SHOP VALUES (NULL,?,?,?,?)",(product,profit,loss,client))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM SHOP")
    rows=curr.fetchall()
    conn.close()
    return rows

def search(product="",profit="",loss="",client=""):
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM SHOP WHERE PRODUCT=? OR PROFIT=? OR LOSS=? OR CLIENT=?",(product,profit,loss,client))
    rows=curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("delete from shop where id=? ",(id,))
    conn.commit()
    conn.close()

def update(id,product,profit,loss,client):
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("update shop set product=? ,profit=?,loss=?,client=? where id=? ",(product,profit,loss,client,id))
    conn.commit()
    conn.close()

def drop():
    conn=sqlite3.connect("Shop.db")
    curr=conn.cursor()
    curr.execute("drop table shop")
    conn.commit()
    conn.close()

#connect()
insert("Gold Chain",1600,0,"Ram")
#update(2,'plarinum',12,3,'DOn')
#delete(4)
#print(search(client="Lakman"))
print(view())
