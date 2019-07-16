import sqlite3
import re

conn = sqlite3.connect('CountingOrganizations.sqlite')
cur = conn.cursor()

#Drop Table if exists
cur.execute('DROP TABLE IF EXISTS Counts')
#Create Table
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname = input('input file name: ')
if(len(fname)<1):fname='mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()
    yy = pieces[1].split('@',1)
    org = yy[1]
    #org = str(re.findall('@([^ ]*)',line))
    cur.execute('SELECT org FROM Counts WHERE org = ?',(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org,count) VALUES(?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
sqlstr = 'SELECT * FROM Counts ORDER BY count DESC'
cur.execute(sqlstr)
conn.commit()

cur.close()
