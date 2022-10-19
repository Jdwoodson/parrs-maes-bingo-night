import sqlite3

db_file = 'bingo.db'
 
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    conn.execute("""
                insert into form_return (form_id, full_name, adults, children, cards, daubers, chicken)
                values
                (1, 'Smith', 2, 2, 10, 4, 2),
                (2, 'Johnson', 4, 5, 5, 2, 2),
                (3, 'Jameson', 2, 2, 10, 4, 2);
                """)
    print('Inserted values into the table!')
print('Closed the connection!')