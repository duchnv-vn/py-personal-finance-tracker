import csv
from datetime import datetime
import inquirer

stop_command = 'stop'

ROOT_DIR = 'csv-app/csv-sources'

CATEGORIES = (
    ('food', 'Food'),
    ('moving', 'Moving'),
    ('laundry', 'Laundry'),
    ('family_support', 'Family support'),
    ('beauty', 'Beauty'),
    ('houseware', 'Houseware'),
    ('party', 'Party'),
    ('entertainment', 'Entertainment'),
    ('education', 'Education'),
    ('monthly_bill', 'Monthly bill'),
    ('others', 'Others'),
)


def exec():
    def select_file():
        FORMAT = '%m-%Y'

        date_str = input('Enter file time (Example: 01-2024):')

        try:
            check_date = datetime.strptime(date_str, FORMAT).strftime(FORMAT)

            if (date_str != check_date):
                raise ValueError()

            return date_str
        except ValueError as error:
            print('INVALID TIME FORMAT')
            select_file()

    def set_day():
        FORMAT = '%d'
        day = input('Enter day (Example: 01): ')

        try:
            check_day = datetime.strptime(day, FORMAT).strftime(FORMAT)

            if (day != check_day):
                raise ValueError()

            return day
        except ValueError as error:
            print('INVALID DAY FORMAT')
            set_day()

    def check_to_stop(item):
        if item == stop_command or item == 'no':
            raise ValueError()

    month_year = select_file()
    day = set_day()

    FILE_NAME = f'{month_year}.csv'

    with open(f'{ROOT_DIR}/{FILE_NAME}', mode="a") as file:
        csv.register_dialect('custom_dialect', lineterminator='\n')
        csv_writer = csv.writer(file, dialect='custom_dialect')

        count_record = 0

        print('=== NOTE ===')
        print(f'enter [{stop_command}] text for stopping add new data')
        print('======')

        try:
            while True:
                if count_record > 0:
                    ask_for_next_select = inquirer.List(
                        'is_next', message='Add more record?', choices=['yes', 'no'])
                    ask_for_next_result = inquirer.prompt(
                        [ask_for_next_select])
                    ask_for_next = ask_for_next_result['is_next']
                    check_to_stop(ask_for_next)

                categories_select = inquirer.List(
                    'category', message='Select category name', choices=[name for (key, name) in CATEGORIES])
                category_result = inquirer.prompt([categories_select])
                category = category_result['category']
                check_to_stop(category)

                expense_name = input('Enter expense name: ')
                check_to_stop(expense_name)

                number = input('Enter money number: ')
                check_to_stop(number)

                description = input('Enter description about expense: ')
                check_to_stop(description)

                data = (day, category, expense_name, number, description)
                csv_writer.writerow(data)
                count_record += 1

                print(f'=== RECORD {count_record} ===')
                print(f'New record data {data}')
                print('======')
        except:
            pass

    print(f'=== SUCCESSFULLY WRITE FILE: {FILE_NAME} ===')


exec()