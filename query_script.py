import sqlite3

#Connect DB
conn = sqlite3.connect('3d_printer_machine_management.db')
cursor = conn.cursor()

#Query Section
cursor.execute(f"""
SELECT * FROM printerFor_{'dang'} """)
result = cursor.fetchone();

#Print query result
print(result)
result = cursor.fetchall();
print(result)

conn.commit()
conn.close()