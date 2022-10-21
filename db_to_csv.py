import csv
import sqlite3
import sys

db_file = sys.argv[1]

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("select * from form_return;")
with open("out.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()