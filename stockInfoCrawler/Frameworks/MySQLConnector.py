__author__ = 'Ryan'

import MySQLdb


class MySQLConnector(object):
    __db_name = ""
    __con = None

    def __init__(self):
        pass

    def connect(self, db_name):
        self.__db_name = db_name
        try:
            self.__con = MySQLdb.connect(host='localhost', user='root', passwd='7758258', db=db_name, port=3306)
        except MySQLdb.Error, e:
            print "Mysql connect error %d: %s" % (e.args[0], e.args[1])

    def close_connect(self):
        self.__con.close()

    def insert_many(self, table, columns, values):
        with self.__con:
            cur = self.__con.cursor()
            col_length = len(columns.split(','))
            column_values = "%s" + ", %s"*(col_length - 1)
            statement = """INSERT INTO %s(%s) VALUES(%s)""" % (table, columns, column_values)
            #print statement
            cur.executemany(statement, values)
            self.__con.commit()
            cur.close()

    def insert(self, table, column, value):
        with self.__con:
            cur = self.__con.cursor()
            statement = """INSERT INTO %s(%s) VALUES(%s)""" % (table, column, value)
            cur.execute(statement)
            cur.close()

    def query(self, table, column, value):
        with self.__con:
            cur = self.__con.cursor()
            statement = """SELECT * FROM %s where %s = %s""" % (table, column, value)
            cur.execute(statement)
            data = cur.fetchall()
            cur.close()
            return data

    def query(self, table, column):
        with self.__con:
            cur = self.__con.cursor()
            statement = """SELECT %s FROM %s""" % (column, table)
            cur.execute(statement)
            data = cur.fetchall()
            cur.close()
            return data




