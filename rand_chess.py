# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
import queens

def generating_random_positions():
    numbers = ['1', '2', '3', '4', '5' , '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f' ]
    new_list = []
    for _ in range(8):
        el1 = random.sample(letters, 1)
        el2 = random.sample(numbers, 1)
        new_element = ''.join(el1 + el2)
        new_list.append(new_element)
        positions = set(new_list)
    return positions


def generating_start_posotion():
    """ Generating start position for the first queen """
    numbers = ['1', '2', '3', '4', '5' , '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f' ]
    new_list = []
    el1 = random.sample(letters, 1)
    el2 = random.sample(numbers, 1)
    new_element = ''.join(el1 + el2)
    new_list.append(new_element)
    start_position = set(new_list)
    return start_position


print(f'\nСлучайно сгенерированные координаты {generating_random_positions()}')
result = queens.place_queens(generating_random_positions())
print(result)
print()
queens.print_board(result)

print('\nВарианты успешной расстановки ферзей.')
variants = 4 # количетсво вариантов согласно условию задачи
count = 1
for _ in range(variants):
    print(f'\nВариант №{count}.')
    start_position = generating_start_posotion()
    print(f'\nГенерация координаты для размещения 1-го ферзя {start_position}')
    result = queens.place_queens(start_position)
    print(f'Координаты успешной расстановки ферзей {result} исходя из сгенерированной начальной координаты {start_position}')
    print()
    queens.print_board(result)
    print()
    count += 1
