import sqlite3
import sys

db_file = sys.argv[1]

def input_data():
    form_id = int(input('Form ID#: '))
    first_name = str(input('First names: '))
    last_name = str(input('Last name: '))
    adults = int(input('Number of adults: '))
    children = int(input('Number of children: '))
    cards = int(input('Number of bingo cards: '))
    daubers = int(input('Number of daubers: '))
    chicken = int(input('Number of sandwiches: '))
    paid = str(input('Full Prepayment?: '))
    data = (last_name, first_name, adults, children, cards, daubers, chicken, paid, form_id)
    with sqlite3.connect(db_file) as conn:
        print('Created the connection!')
        conn.execute("""
                UPDATE form_return
                SET last_name = ?,
                first_name = ?,
                adults = ?,
                children = ?,
                cards = ?,
                daubers = ?,
                chicken = ?,
                paid = ?
                WHERE form_id = ?
                """, data)
        print('Updated values in the DB!')
        
def main():
    while True:
        input_data()       
 
if __name__ == '__main__':
    main()