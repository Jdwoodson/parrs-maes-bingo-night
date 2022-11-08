import csv
import sqlite3
import sys

db_file = sys.argv[1]

rsvp_dict = {}
paid_rsvp = []
unpaid_rsvp = []
chicken_purchase = []
 
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   select * from form_return
                   """)
    for row in cursor.fetchall():
        form_id, last_name, first_name, adults, children, cards, daubers, chicken, paid = row
        rsvp_dict[form_id] = {'last_name':last_name, 'first_name':first_name, 'cards':cards, 'daubers':daubers, 'chicken':chicken, 'paid':paid, 'form_id':form_id}
        # print("{} {}:\n"
        #       "------------ {}\n"
        #       "Adults:           {}\n"
        #       "Children:         {}\n"
        #       "Num of Cards:     {}\n"
        #       "Num of Daubers:   {}\n"
        #       "Num of Chicken:   {}\n"
        #       "Paid status:      {}\n\n".format(first_name, last_name, form_id, adults, children, cards, daubers, chicken, paid))

# print(rsvp_dict)

for rsvp in rsvp_dict:
    # print(rsvp_dict[rsvp])
    form_id = rsvp_dict[rsvp].get('form_id')
    last_name = rsvp_dict[rsvp].get('last_name')
    first_name = rsvp_dict[rsvp].get('first_name')
    cards = rsvp_dict[rsvp].get('cards')
    daubers = rsvp_dict[rsvp].get('daubers')
    chicken = rsvp_dict[rsvp].get('chicken')
    paid = rsvp_dict[rsvp].get('paid')
    if rsvp_dict[rsvp].get('paid') == 'no':
        unpaid_rsvp.append({'last_name':last_name, "first_name":first_name, 'cards':cards, 'daubers':daubers})
    if rsvp_dict[rsvp].get('paid') == 'yes':
        paid_rsvp.append({'last_name':last_name, "first_name":first_name, 'cards':cards, 'daubers':daubers, 'chicken':chicken})
    if rsvp_dict[rsvp].get('paid') == 'yes':
        if rsvp_dict[rsvp].get('chicken') > 0:
            chicken_purchase.append({'last_name':last_name, "first_name":first_name, 'chicken':chicken})

def getLastName(rsvp):
    return rsvp.get('last_name')

# print(unpaid_rsvp)

unpaid_rsvp.sort(key=getLastName)

paid_rsvp.sort(key=getLastName)

chicken_purchase.sort(key=getLastName)


with open("unpaid.csv", 'w',newline='') as csv_file:
    fieldnames = ['last_name', 'first_name', 'cards', 'daubers']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for rsvp in unpaid_rsvp:
        writer.writerow(rsvp)

with open("paid.csv", 'w',newline='') as csv_file:
    fieldnames = ['last_name', 'first_name', 'cards', 'daubers', 'chicken']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for rsvp in paid_rsvp:
        writer.writerow(rsvp)

with open("chicken.csv", 'w',newline='') as csv_file:
    fieldnames = ['last_name', 'first_name', 'chicken']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for rsvp in chicken_purchase:
        writer.writerow(rsvp)