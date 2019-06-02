import json
import datetime

print("Hello to SheetOne.")

salary = 2000.50


def check_date():
    print("Hello from a function")
    currentDay = int(datetime.datetime.now().strftime('%d'))
    # Open JSON file and check date
    with open('expenses/staticExpensesMonthly') as json_file:
        data = json.load(json_file)
        for d in data['staticExpensesMonthly']:
            print('Name: ' + d['name'])
            print('Debit date: ' + str(d['debit_date']))
            debit_date = d['debit_date']

            print(currentDay)
            print(debit_date)
            boDebited = currentDay > debit_date
            print(boDebited)
            print('')

            # Write debited boolean in JSON
            # data['staticExpensesMonthly'].append({'b': '2'})
            # json.dumps(data)


# create group of expenses (see staticExpensesMonthly JSON)

# with open('expenses/staticExpensesMonthly') as json_file:
#     data = json.load(json_file)
#     sum = 0
#     for p in data['staticExpensesMonthly']:
#         print('Name: ' + p['name'])
#         print('Price: ' + str(p['price']))
#         print('')
#         sum += (p['price'])

# print(salary - sum)
# print(datetime.datetime.now())

check_date()

# Setup boolean for booked/non-booked; default no; every single startup json
# will be checked and if date is later than booking date, then set book to true

