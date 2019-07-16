import sqlite3

conn = sqlite3.connect('OurFirstDatabase.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('CREATE TABLE Ages (name VARCHAR(128),age INTEGER)')
cur.execute('DELETE  FROM Ages')
while True:
    end = input('end or continue: ')
    if end == 'end':break
    name = input('input the name: ')
    age = input('input the age: ')

    cur.execute('SELECT name FROM Ages WHERE name = ?',(name,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Ages(name,age) VALUES(?,?)',(name,age))
    else:
        cur.exceute('UPDATE Ages SET (name=?,age=?)',(name,age))

conn.commit()
sqlstr = ' SELECT hex(name || age) AS X FROM Ages ORDER BY X'
cur.execute(sqlstr)
data = cur.fetchone()
print(data)

cur.close()
