# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

""" Safe placement of 8 queens """


# перевод координат из строки в пару (ряд, столбец): "b1" -> (0,1)
str2coord = lambda s: (int(s[1])-1, ord(s[0])-ord('a'))

# обратная функция
coord2str = lambda c: chr(c[1]+ord('a'))+str(c[0]+1)

# проверка что 2 ферзя не бьют труг друга
def can_be_placed(p1, p2):
    (r1,c1), (r2,c2) = p1, p2
    return r1 != r2 and c1 != c2 and abs(r2-r1) != abs(c2-c1)

# проверка что новый ферзь не бьёт ни один из уже установленных
can_be_placed_on_board = lambda queens, pos: all(can_be_placed(p, pos) for p in queens)

# проверка на занятость ряда
is_row_occupied = lambda queens, r: sum(1 for p in queens if p[0]==r)


def place_one_queen(queens, r):
    # в списке 8 ферзей - значит всех расставили
    if len(queens) == 8: return set(map(coord2str, queens))
    # вышли за границу доски - тут нам делать нечего
    if r == 8: return set()
    if is_row_occupied(queens, r):
        # в текущем ряду уже занято - попытаемся в следующем
        return place_one_queen(queens, r+1)
    for c in range(8):
        # идём по столбцам и пытаемся поставить ферзя
        if can_be_placed_on_board(queens, (r,c)):
            # можно поставить - ставим и переходим на следующий ряд
            result = place_one_queen(queens+[(r,c)], r+1)
            # вернулись с результатом - значит дальше можно не искать - возвращаемся и передаём результат выше 
            if result: return result
    return set()


def place_queens(positions):
    queens = []
    # размещаем исходных ферзей и проверяем, что они не бьют друг друга
    for pos in positions:
        coord = str2coord(pos)
        if not can_be_placed_on_board(queens, coord):
            print('Размещение по указанным координатам невозможно')
            return set()
        queens.append(coord)

    return place_one_queen(queens, 0)


# просто печатаем положение ферзей на доске (для наглядности)
def print_board(queens):
    coords = list(map(str2coord, queens))
    print(' ', *list(map(chr, range(65, 65+8))))
    for r in range(7,-1,-1):
        print(r+1, end=' ')
        for c in range(8):
            print('X' if (r,c) in coords else '.', end=' ')
        print(r+1)
    print(' ', *list(map(chr, range(65, 65+8))))
