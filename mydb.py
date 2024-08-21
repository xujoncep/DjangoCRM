import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='$onarBangla25',
)

# prepare a coursor object

cursorObject = database.cursor()

# create database

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")
