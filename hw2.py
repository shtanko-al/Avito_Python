# отрисовка игрового поля:
def print_pole():
    for i in pole:
        for j in i:
            print(j, end=' ')
        print()


def in_coord(): # ввод координат клетки
    while True:
        co = [int(i) for i in input().split()]
        if pole[co[0] - 1][co[1] - 1] != '*':
            print("Эта клетка занята, введите другую")
        else:
            break
    return co

def size_pole_input(): # ввод размеров поля, с проверкой
    while True:
            siz = input()
            if siz.isdigit() and int(siz) >2 and int(siz)<6:
                siz_dit = int(siz)
                break
            else:
                print("Введите число от 3 до 5")
                #siz = input()
    return siz_dit

def chek_win(symb_player :str):
    n = 0

    for i in range(size_pole):
        n = 0
        for j in range(size_pole):
            if pole[i][j] == symb_player:
                n = n + 1
        if n == size_pole:
            break

    if n != size_pole:
        for i in range(size_pole):
            n = 0
            for j in range(size_pole):
                if pole[j][i] == symb_player:
                    n = n + 1
            if n == size_pole:
                break

    if n != size_pole:
        n = 0
        for i in range(size_pole):
            if pole[i][i] == symb_player:
                n = n + 1

    if n != size_pole:
        n = 0
        for i in range(size_pole):
            if pole[i][i] == symb_player:
                n = n + 1

###########################
coord = list()
symb_p1 = 'x'
symb_p1 = '0'
print("Игра крестики-нолики")
print("Введите размер поля (от 3 до 5):")
size_pole = size_pole_input()
# генерация начального поля:
pole = [['*'] * size_pole for i in range(size_pole)]

print("Введите координаты клетки, через запятую:")
coord = in_coord()
pole[coord[0] - 1][coord[1] - 1] = 'x'
print(coord)  # для отладки

print("Введите координаты клетки, через запятую:")
coord = in_coord()
pole[coord[0] - 1][coord[1] - 1] = '0'
print(coord)  # для отладки

print_pole()
