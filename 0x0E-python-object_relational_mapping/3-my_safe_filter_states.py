#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(user=sys.argv[1],
                         host="localhost",
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states\
                    WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    for i in myCursor.fetchall():
        print(i)
    db.close()
