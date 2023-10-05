# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description='Проверка даты.')
parser.add_argument('date', type=str, help='Формат даты ГГГГ-ММ-ДД')

args = parser.parse_args()

print(validate_date(args.date))