import sqlite3
import sys

db_file = sys.argv[1]

def input_data():
    form_id = int(input('Form ID#: '))
    full_name = str(input('First and Last name: '))
    adults = int(input('Number of adults: '))
    children = int(input('Number of children: '))
    cards = int(input('Number of bingo cards: '))
    daubers = int(input('Number of daubers: '))
    chicken = int(input('Number of sandwhiches: '))
    data = (form_id, full_name, adults, children, cards, daubers, chicken)
    with sqlite3.connect(db_file) as conn:
        print('Created the connection!')
        conn.execute("""
                insert into form_return(form_id, full_name, adults, children, cards, daubers, chicken)
                values(?,?,?,?,?,?,?)
                """, data)
        print('Inserted values into the table!')
        
def main():
    while True:
        input_data()       
 
if __name__ == '__main__':
    main()