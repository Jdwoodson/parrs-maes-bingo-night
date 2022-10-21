import sqlite3
import sys

db_file = sys.argv[1]
 
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   select * from form_return
                   """)
    for row in cursor.fetchall():
        form_id, full_name, adults, children, cards, daubers, chicken = row
        print("{}:\n"
              "------------ {}\n"
              "Adults:           {}\n"
              "Children:         {}\n"
              "Num of Cards:     {}\n"
              "Num of Daubers:   {}\n"
              "Num of Chicken:   {}\n\n".format(full_name,form_id, adults, children, cards, daubers, chicken))