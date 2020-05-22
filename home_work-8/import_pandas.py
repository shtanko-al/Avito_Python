import os
import time
import pandas as pd

DIR = 'other_user_logs'


# def prepare_train_set(logs_path: str, session_length: int, window_size: int, max_duration: int):
def loader_csv(logs_path: str):
    """"
    функция загружает файлы csv из папки, возвращает объект Pandas
    logs_path - имя папки с файлами для загрузки
    """
    csv_files_list = [f for f in os.listdir(logs_path) if f[-3:] == 'csv']  # выборка только csv
    if len(csv_files_list) == 0:
        raise Exception('в папке {} нет csv файлов'.format(logs_path))

    file = open('{}./{}'.format(logs_path, csv_files_list[0]), 'r')
    column_name = file.readline().strip().split(',')  # названия для второго и третьего столбца:
    file.close()                                      # для сравнения с остальными файлами

    data_list = []  # список словарей с данными для DataFrame
    for file_name in csv_files_list:
        with open('{}./{}'.format(logs_path, file_name), 'r') as file_to_read:
            new_column_name = file_to_read.readline().strip().split(',')
            if new_column_name != column_name:  # проверка, что у всех файлов правильная структура заголовков
                raise Exception('файл {} или {} с неправильной структурой'.format(file_name, csv_files_list[0]))
            user_name = file_name[0:file_name.find('.')]  # на всякий случай, если имена у файлов с разной структурой
            for line in file_to_read:
                line_data = line.strip().split(',')
                temp_dict = {
                    'user_id': user_name,
                    column_name[0]: line_data[0],
                    column_name[1]: line_data[1]
                }
                data_list.append(temp_dict)
    return pd.DataFrame(data_list)


if __name__ == '__main__':
    startTime = time.perf_counter()

    super_frame = loader_csv('other_user_logs')
    print('время работы скрипта 1: ', time.perf_counter() - startTime)

    print(super_frame.info())
