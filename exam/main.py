from random import randint

print('Введите количество кустов (не меньше 3)')
size = input()
while True:
    if size.isdigit() and int(size) >= 3:
        size = int(size)
        break
    else:
        print('Введите число больше 3')
        size = input()

kusts = [randint(0, 51) for _ in range(size)]
print(kusts)

kusts.insert(0, kusts[-1])
kusts.append(kusts[1])
max = kusts[-1] + kusts[0] + kusts[1]

poz = 0
for i in range(1, size + 1):
    temp_max = kusts[i - 1] + kusts[i] + kusts[i + 1]
    if temp_max > max:
        max = temp_max
        poz = i - 1

print('индекс нужного куста: ', poz)
