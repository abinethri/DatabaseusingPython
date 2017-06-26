# Counting email in a Database
# assignment: Count the emails (FROM:) in a file and find the highest email domain address 
import sqlite3

conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1].split('@')
    print email[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email[1], ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( email[1], ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (email[1], ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()
    
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT * FROM Counts WHERE count IN  (SELECT max(count) FROM Counts)'

print
print "The Highest email was from: "

for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()


    
