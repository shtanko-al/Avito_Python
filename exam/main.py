kusts = [2, 11, 7, 1, 8, 1]


def berry_coun(k: list):
    if len(k) < 3:
        raise ImportError

    kusts = k
    kusts.insert(0, kusts[-1])
    kusts.append(kusts[1])
    max = kusts[-1] + kusts[0] + kusts[1]

    poz = 0
    for i in range(1, len(kusts) - 1):
        temp_max = kusts[i - 1] + kusts[i] + kusts[i + 1]
        if temp_max > max:
            max = temp_max
            poz = i - 1
    return poz


if __name__ == '__main__':
    k_list_1 = [0, 1, 2, 3, 4, 5, 6, 7]
    k_list_2 = [1, 2, 3]
    k_list_3 = [0, 1]

    print(berry_coun(k_list_1))
    print(berry_coun(k_list_2))
    print(berry_coun(k_list_3))
