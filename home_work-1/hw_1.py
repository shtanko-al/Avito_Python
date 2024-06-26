# вместо утки, основа для квеста:

action_num = 1


class Inventory:
    def __init__(self, volume_max):
        self.volume = 0  # текущая заполненность инвентаря
        self.volume_max = volume_max  # максимальная емкость инвентаря
        self.inv_list = list()

    def take(self, item: dict):
        if self.volume + item["veight"] <= self.volume_max:
            self.volume += item["veight"]
            self.inv_list.append(item)

    def show_inv(self):
        print(self.inv_list)


def celect_action():
    global action_num
    print('1) Осмотреться')
    print('2) Проверить карманы')
    print('3) Подумать о самочувствии')
    action = input()
    while True:
        if action.isnumeric() and 1 <= int(action) <= 3:
            action_num = int(action)
            break
        else:
            print('В ведите номер ответа')
            action = input()


def look_arraund(area_num: int, mod_num=1):
    area_map = {1: 'лес',
                2: 'пещера',
                3: 'поле',
                4: 'деревня',
                }
    mod_map = {1: 'все хорошо',
               2: 'подозрительно',
               3: 'опасно',
               }
    print('вы находитесь в {:s}, все выглядит {:s}\n'.format(area_map[area_num], mod_map[mod_num]))


def my_action(action_num):
    if action_num == 1:
        look_arraund(2, 1)


#############################
print("Вы находитесь на поляне в лесу, на поляне дерево, под ним сундук")
print("Ваши действия:")
celect_action()
my_action(action_num)

inventory_1 = Inventory(30)

inventory_1.take({
    "name": "iron sword",
    "veight": 3,
})
inventory_1.take({
    "name": "red apple",
    "veight": 1,
})
print(inventory_1.volume)
print(inventory_1.volume_max)
inventory_1.show_inv()
