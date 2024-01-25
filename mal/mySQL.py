import time

import mysql.connector

testdb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='LmA7ZTyx120!#',
    database='logs'
)

dbcursor = testdb.cursor()


# creates a database
# remember to remove the database argument from the testdb above
# example use create_db(users)
def create_db(name):
    query = "CREATE DATABASE {}".format(name)
    dbcursor.execute(query)


# show tables in the database
# example use: show_tables()
def show_tables():
    dbcursor.execute("SHOW TABLES")

    for table in dbcursor:
        print(table)


# creates a table in the database
# example: create_table('logs', '(date VARCHAR(255), logs VARCHAR(255))')
def create_table(table_name, table_rows):
    query = "CREATE TABLE {} {}"
    query = query.format(table_name, table_rows)
    dbcursor.execute(query)


def drop_table(table):
    query = "DROP TABLE {}".format(table)
    dbcursor.execute(query)


# show all rows in a table
# example use: show_rows(logs)
def show_rows(table):
    query = "SELECT * FROM {}"
    query = query.format(table)
    dbcursor.execute(query)

    for row in dbcursor:
        print(row)
    return dbcursor


# Adds rows to your database
# example: add_rows('logs', '(date, logs)', '("todays date", "the log string")')
def add_rows(table, columns, values):
    query = "INSERT INTO {} {} VALUES {}"
    query = query.format(table, columns, values)
    dbcursor.execute(query)

    testdb.commit()


# update existing entry
def update_row(table, new_column, new_row, old_column, old_row):
    query = "UPDATE {} SET {} = {} WHERE {} = {}"
    query = query.format(table, new_column, new_row, old_column, old_row)
    dbcursor.execute(query)

    testdb.commit()


