import sqlite3

db = sqlite3.connect('TestingLoggs.db')  
cursor = db.cursor() 


# cursor.execute('''CREATE TABLE Testing (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             datetime text,
#             scenario_name text,
#             scenario_status text,
#             scenario_message text
#             )''')




cursor.execute("SELECT * FROM Testing")

for x in cursor:
    print(x)



