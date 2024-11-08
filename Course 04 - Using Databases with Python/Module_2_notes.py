'''
Video - 15.1
Topic - Relational Databases
'''

'''
Relational databases model data by storing rows and columns in tables. The power of the relational database lies in its ability to efficiently retrieve data from those tables and in particular where there are multiple tables and the relationships between those tables involved in the query.
'''

'''
SQL -  Structured Query Language is the language we use to issue 
commands to the database.

• Create a table
• Read / Retrieve some data
• Update / Insert data
• Delete data

Is also known as CRUD operation in Databases.
'''



'''
Video - 15.3
Topic - Single Table CRUD
'''

'''
* Create A single table:

CREATE TABLE Users(
    name VARCHAR(128),
    email VARCHAR(128)
)


* SQL Insert:
• The Insert statement inserts a row into a table.


INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')


* Multiple row insertion:

INSERT INTO Users (name, email) VALUES 
	('Tabit', 'tab3423@gmail.com'),
	('Karim', 'karim1143@gmail.com'),
	('Slime', 'slime34@yahoo.com'),
	('Hop', 'hop556@gamil.com'),
	('Puth', 'puth@gov.edu.org');



* SQL Delete:
• Deletes a row in a table based on a selection criteria.

DELETE FROM Users WHERE email='sush@nyu.edu.us'



* SQL Update:
• Allows the updating of a field with a where clause.

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'



* Retrieving Records - Select:
• The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause.


SELECT * FROM Users

SELECT * FROM Users WHERE email='csev@umich.edu'



* Sorting with ORDER BY:
• You can add an ORDER BY clause to SELECT statements to get
the results sorted in ascending or descending order.

SELECT * FROM Users ORDER BY name 
SELECT * FROM Users ORDER BY email 
'''

