import sqlite3

con = sqlite3.connect("employee.db")
print("Database opened successfully")

con.execute("create table Emp(id integer primary key autoincrement, name text not null, email text unique not null)")
print("Table created")
