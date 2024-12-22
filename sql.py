import sqlite3

##connet to the sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record, create table,retrive
cursor=connection.cursor()

# create a table
table_info="""
Create table STUDENT (NAME VACHAR(25),CLASS VARCHAR(25),SECTION VACHAR(25),MARKS INT);


"""
                                        
cursor.execute(table_info)

#Insert some more record

cursor.execute('''Insert into STUDENT Values('Krishna','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT Values('Suharshu','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT Values('Dariouis','Data Science','A',96)''')
cursor.execute('''Insert into STUDENT Values('Vikashi','AI ','B',50)''')
cursor.execute('''Insert into STUDENT Values('Dipeshi','DEVOLPS','A',70)''')

##Display all the records
print("The Inserted records are ")

data=cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)

##close the connection
connection.commit()
connection.close() 
