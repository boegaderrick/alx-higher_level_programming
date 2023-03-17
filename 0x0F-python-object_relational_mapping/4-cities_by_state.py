#!/usr/bin/python3
"""This script accesses mysql databases using the MySQLdb module"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    h = 'localhost'
    p = 3306
    u = sys.argv[1]
    pw = sys.argv[2]
    d = sys.argv[3]
    try:
        db = MySQLdb.connect(host=h, port=p, user=u, passwd=pw, db=d)
        cursor = db.cursor()
        query = 'SELECT cities.id, cities.name, states.name FROM cities JOIN\
            states WHERE cities.state_id = states.id ORDER BY cities.id ASC'
        cursor.execute(query)
        for r in cursor.fetchall():
            print(r)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)
