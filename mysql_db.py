# Install using below command# pip install mysql-connector-python 
import mysql.connector
import os

sql_host = "erpstgdev.cluster-c6rhkodfxytn.us-east-1.rds.amazonaws.com"
sql_username = "JENKINSPOC_USER"
sql_password = os.getenv("sql_password")
sql_database = "JENKINSPOC"

mysqlConn = mysql.connector.connect(host= sql_host, user= sql_username, password= sql_password, database= sql_database)

mycursor = mysqlConn.cursor()

tableName = "builds"

mycursor.execute("SELECT * FROM {tableName}".format(tableName = tableName))

myresult = mycursor.fetchall()

print(type(myresult))
print("\n\n\n")

for x in myresult:
    print(type(x))
    print(x)
    print("\n\n\n")
