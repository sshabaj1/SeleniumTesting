import sqlite3

db = sqlite3.connect('TestingLoggs.db')  # You can create a new database by changing the name within the quotes
cursor = db.cursor() # The database will be saved in the location where your 'py' file is saved


# cursor.execute('''CREATE TABLE Testing (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             datetime text,
#             scenario_name text,
#             scenario_status text,
#             scenario_message text
#             )''')


# cursor.execute("""CREATE TABLE Scenarios (
#             id intiger,
#             datatime text,
#             scenario_name text,
#             scenario_status text,
#             scenario_message text
#             )""")
                       

cursor.execute("SELECT * FROM Testing")

for x in cursor:
    print(x)



