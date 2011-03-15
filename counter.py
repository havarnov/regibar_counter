#!/usr/bin/env python2

import psycopg2,time

#connect to database
db='dbname'
username='username'
passwd='secret'
hostname='hostname'

conn = psycopg2.connect(database=db,user=username,password=passwd,host=hostname)

#open a cursor to perform db operations
cur = conn.cursor()

#perform operations
tabel = 'tablename'
t = int(time.time())

cur.execute('INSERT INTO %s (time) VALUES %s',(table,t)) 

#commit changes to db
conn.commit()

#close connection
cur.close()
conn.close()
