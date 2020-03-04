def print_pole():  # отрисовка игрового поля
    for i in pole:
        for j in i:
            print(j, end=' ')
        print()


def in_coord():  # ввод координат клетки
    # co = []
    # while True:
    #     co = input().split()
    #     #co = [int(i) for i in input().split()]
    #     if len(co) == 2:
    #         for i in [0, 1]:
    #             if co[i].isdigit() and int(co[i])>0 and int(co[i])<size_pole:
    #             co[i] = int(co[i])
    #     else:
    #         print("Не правильно введены координаты, повторите ввод")

    while True:
        coords = input().split()
        if len(coords) > 2:
            print('Введите ровно 2 числа')
            continue

        row, column = [int(coord) for coord in coords]
        if row > size_pole or column > size_pole:
            print('You entered some shit')
            continue

        if pole[int(row) - 1][int(column) - 1] != '*':
            print("Эта клетка занята, введите другую")
        else:
            break
    return row, column


def size_pole_input():  # ввод размеров поля, с проверкой
    while True:
        siz = input()
        if siz.isdigit() and 2 < int(siz) < 6:
            siz_dit = int(siz)
            break
        else:
            print("Введите число от 3 до 5")
            # siz = input()
    return siz_dit


def check_row(data: list, symbol: str) -> bool:
    for player_move in data:
        if player_move != symbol:
            return False

    return True


def chek_win(symb_player: str):
    for i in range(size_pole):
        if check_row(pole[i], symb_player):
            return 1

    for i in range(size_pole):
        column = [pole[j][i] for j in range(size_pole)]
        if check_row(column, symb_player):
            return 1

    # for i in range(size_pole):
    #     n = 0
    #     for j in range(size_pole):
    #         if pole[i][j] == symb_player:
    #             n = n + 1
    #     if n == size_pole:
    #         break

    data = [pole[i][i] for i in range(size_pole)]
    if check_row(data, symb_player):
        return 1

    data = [pole[i][size_pole - i - 1] for i in range(size_pole)]
    if check_row(data, symb_player):
        return 1

    return 0
    # if n != size_pole:
    #     for i in range(size_pole):
    #         n = 0
    #         for j in range(size_pole):
    #             if pole[j][i] == symb_player:
    #                 n = n + 1
    #         if n == size_pole:
    #             break
    #
    # if n != size_pole:
    #     n = 0
    #     for i in range(size_pole):
    #         if pole[i][i] == symb_player:
    #             n = n + 1
    #
    # if n != size_pole:
    #     n = 0
    #     for i in range(size_pole):
    #         if pole[i][size_pole - i - 1] == symb_player:
    #             n = n + 1
    # if n == size_pole:
    #     return 1
    # else:
    #     return 0


###########################
if __name__ == '__main__':
    coord = list()
    symb_p1 = 'x'
    symb_p2 = '0'
    print('Игра крестики-нолики')
    print("Введите размер поля (от 3 до 5):")
    size_pole = size_pole_input()
    # генерация начального поля:
    pole = [['*'] * size_pole for i in range(size_pole)]

    # print("Введите координаты клетки, через запятую:")
    # coord = in_coord()
    # pole[coord[0] - 1][coord[1] - 1] = symb_p1
    # print(coord)  # для отладки
    #
    # print("Введите координаты клетки, через запятую:")
    # coord = in_coord()
    # pole[coord[0] - 1][coord[1] - 1] = symb_p2
    # print(coord)  # для отладки

    print_pole()
    step_number = 0
    while True:
        n = 1
        print()
        print("ход игрока", n)
        print("Введите координаты клетки, через запятую:")
        coord = in_coord()
        pole[coord[0] - 1][coord[1] - 1] = symb_p1
        print_pole()
        if chek_win(symb_p1) == 1:
            print("Игрок 1 победил, игра окончена")
            break

        n = 2
        print()
        print("ход игрока", n)
        print("Введите координаты клетки, через запятую:")
        coord = in_coord()
        pole[coord[0] - 1][coord[1] - 1] = symb_p2
        print_pole()
        if chek_win(symb_p2) == 1:
            print("Игрок 2 победил, игра окончена".format(n))
            break

        step_number += 1

        if size_pole ** 2 == step_number:
            print('Ничья')
            break
