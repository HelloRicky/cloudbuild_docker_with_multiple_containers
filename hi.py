#!/usr/bin/python
import psycopg2
hostname = 'localhost'
username = 'USERNAME'
password = 'PASSWORD'
database = 'ricky'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()


print("Using psycopg2…")

myConnection = psycopg2.connect( host=hostname, user='test', password='test', dbname=database )
doQuery( myConnection )
myConnection.close()