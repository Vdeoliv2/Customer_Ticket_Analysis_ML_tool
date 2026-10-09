import pandas as pd # loads pandas library operates with structured/tabular data
import sqlite3 # loads the database management system that stores the structured data in a database and query it in SQL

df = pd.read_csv("data/raw/customer_support_tickets.csv")# asks pandas to read the csv file in the path and assigns the dataframe to a variable df

connection = sqlite3.connect("customer_support.db") # returns a connection object that connects SQLite's created database to the variable connection

df.to_sql(#sends a Pandas dataframe into a SQL database as a table
    "tickets", # name of the new SQL table
    connection, # the location of the database the tickets table is stored
    if_exists = "replace", # if a tickets table already exists, it deletes the existing table and creates a new one with the current data
    index = False # asks not to create an additional SQL column for the Pandas index
)


cursor = connection.cursor() # creates a cursor object to send the SQL commands to SQLite and access their results

cursor.execute("SELECT * FROM tickets LIMIT 10;")# cursor exectues the SQL statement

rows = cursor.fetchall() # retrieves all remaning rows produced by a query

for row in rows:
    print(row)

connection.close() # closes the conection to the SQL database

print("Dataabase created successfully!")
