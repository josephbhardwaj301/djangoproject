import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="user",
passwd ="gfg"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE FIRSTSQL")
