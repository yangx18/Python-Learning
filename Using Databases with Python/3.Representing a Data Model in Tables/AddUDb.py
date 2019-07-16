import sqlite3
from openpyxl import load_workbook

conn = sqlite3.connect('AddUDb.sqlite')
cur = conn.cursor()

cur.executescript('''

Drop TABLE IF EXISTS Artist;
Drop TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    rating INTEGER,
    artist_id INTEGER
);

''')
fname = input('file name :')
if (len(fname)<1):fname = 'music.xlsx'

workbook = load_workbook(fname)
sheets = workbook.get_sheet_names()
worksheet = workbook.get_sheet_by_name(sheets[0])
for row in worksheet.rows:
    for cell in row:
        if (row[0] == 'song'):continue
    print(row.value)
