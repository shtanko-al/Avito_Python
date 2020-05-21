import os
import time
import pandas as pd


# def prepare_train_set(logs_path: str, session_length: int, window_size: int, max_duration: int):
def csv_loader(logs_path: str):
    dir = os.listdir(logs_path)
    # print(dir)
    # csv_files_list = (f for f in dir if dir[-3:] == 'csv')
    # print('длна:', len(csv_files_list))
    # print(csv_files_list)
    # for i in csv_files_list:
    #     print(i)
    data_list = []
    for file_name in dir:
        # print('file_name = ', file_name)
        # print('./{}'.format(file_name))
        with open('{}./{}'.format(logs_path, file_name), 'r') as file_to_read:
            temp_title = file_to_read.readline().rstrip().split(',')
            file_title = [file_name[0:-4], temp_title[0], temp_title[1]]
            for line in file_to_read:
                line_data = line.rstrip().split(',')
                temp_dict = {
                    'user_id': file_title[0],
                    file_title[1]: line_data[0],
                    file_title[2]: line_data[1]
                }
                data_list.append(temp_dict)
    return pd.DataFrame(data_list)


if __name__ == '__main__':
    startTime = time.perf_counter()
    super_frame = csv_loader('sample_2')
    print('время работы скрипта {} секунд'.forma(time.perf_counter() - startTime))
