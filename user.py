import sqlite3
  
con = sqlite3.connect("pythondemo.db")  
print("Database opened successfully")  
  
con.execute("create table Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close() 