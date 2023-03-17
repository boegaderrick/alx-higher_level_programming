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
    name = sys.argv[4]
    try:
        db = MySQLdb.connect(host=h, port=p, user=u, passwd=pw, db=d)
        cursor = db.cursor()
        query = 'SELECT cities.name FROM cities WHERE cities.state_id = \
            (SELECT states.id FROM states WHERE name LIKE BINARY %s)'
        cursor.execute(query, (name,))
        res = cursor.fetchall()
        for i in range(len(res)):
            if (i > 0):
                print(', ', end='')
            print(res[i][0], end='')
        print()
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)
