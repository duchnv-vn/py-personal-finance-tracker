import csv
from datetime import datetime

ROOT_DIR = 'csv-app/csv-sources'


def select_time():
    FORMAT = '%m-%Y'

    input('Enter file time (Example: 01-2024):')

    try:
        check_date = datetime.strptime(date_str, FORMAT).strftime(FORMAT)

        if (date_str != check_date):
            raise ValueError()

        return date_str
    except ValueError as error:
        print('INVALID TIME FORMAT')
        select_time()


month_year = select_time()

FILE_NAME = f'{month_year}.csv'

HEADER_NAMES = (
    ('day', 'Day'),
    ('category', 'Category name'),
    ('expense_name', 'Expense name'),
    ('number', 'Number'),
    ('description', 'Description')
)

with open(f'{ROOT_DIR}/{FILE_NAME}', mode="w") as file:
    csv.register_dialect('custom_dialect', lineterminator='\n')
    csv_writer = csv.writer(file, dialect='custom_dialect')

    csv_writer.writerow((name for (key, name) in HEADER_NAMES))

print(f'=== SUCCESSFULLY CREATE FILE: {FILE_NAME} ===')
