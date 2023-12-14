# python with sql lite3 - i just curious
# https://www.youtube.com/watch?v=byHcYRpMgI4
# starts around 11:47
# no need to pip install anything, it's already there

import sqlite3 as sql3


# can also create database to just exist in ram
# conn = sqlite3.connect(':memory:')

# video is about a saved database
# create database
# this is "setting up connection"
conn = sql3.connect('customer.db')

c = conn.cursor()

# "using a doc string"
# sql lite is case sensitive

c.execute("""CREATE TABLE customers(
    first_name DATATYPE,
    last_name DATATYPE,
    email DATATYPE

)""")