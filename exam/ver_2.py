def berry_coun(k: list):
    if len(k) < 3:
        raise ImportError

    max = k[-1] + k[0] + k[1]
    poz = 0

    for i in range(1, len(k) - 1):
        temp_max = k[i - 1] + k[i] + k[i + 1]
        if temp_max > max:
            max = temp_max
            poz = i

    if k[-2] + k[-1] + k[0] > max:
        poz = len(k) - 1

    return poz


if __name__ == '__main__':
    k_list_1 = [0, 1, 2, 3, 4, 5, 6, 7]
    k_list_2 = [1, 2, 3]
    # k_list_3 = [0, 1]

    print(berry_coun(k_list_1))
    print(berry_coun(k_list_2))
    # print(berry_coun(k_list_3))
    print(k_list_2)
