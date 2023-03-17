#!/usr/bin/python3
"""This script shows values in a database by means of mysqldb module"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    h = 'localhost'
    p = 3306
    u = sys.argv[1]
    pw = sys.argv[2]
    d = sys.argv[3]
    try:
        db = MySQLdb.connect(host=h, port=p, user=u, passwd=pw, db=d)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM states ORDER BY states.id')
        print('\n'.join(str(r) for r in cursor.fetchall()))
        cursor.close()
        db.close()
    except (MySQLdb.Error):
        pass
