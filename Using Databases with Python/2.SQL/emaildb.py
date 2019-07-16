import sqlite3

##connect with database by sqlite3.connect('database')
##get cursor for execute, refer, and get Result

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()


##cur.execute('DROP TABLE IF EXISTS Counts')
try:
    cur.execute('''
    CREATE TABLE Counts (email TEXT, count INTEGER)''')
except:
    print('update')
else:
    print('created new table')

fname = input('Enter file name: ')
if len(fname)>15:
    email = fname
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) ##email = ? to avoid rejection
    ##query the next one row
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))

    ##handin request
    conn.commit()
    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
    cur.execute(sqlstr)
    data = cur.fetchall() #get the whole row from db
    #for row in cur.execute(sqlstr):
    for row in data:
        print(str(row[0]), row[1])

    ## close cur
    cur.close()
    exit()

if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    ##row = cur.fetchall()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    ##handin request
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
