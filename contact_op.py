from dataclasses import dataclass
from os.path import exists



def write_contact(user, data):
    data.append(user)


def write_data(data, columns):
    with open (file_base, "w", encoding = 'UTF = 8') as f:
        f.write(', '.join(columns) + '\n')
        for user in data:
            f.write(', '.join(user.values()) + '\n')

def add_column(data, column, columns):
    for user in data:
        user[column] = ''
    columns.append(column)
    return data


def read_data():
    valid = exists(file_base)
    if not valid:
        return []
    with open (file_base, "r", encoding = 'UTF = 8') as f:
        data = f.read()
        if len(data.split()) < 2:
            return[]
        columns = data[0].strip().split(', ')
        data = [{columns[i]: user.strip().split(', ')[i] for i in range(len(columns))} for user in data.split()[1:]]
        return data


def get_columns(data):
    if not data:
        return ['Фамилия', 'Имя']
    columns = data[0].keys()
    return columns


def find_contact(data):
    column = input('Введите нужную колонку: ')
    val = input('Введите значение поиска: ')
    flag = False
    for user in data:
        if column not in data:
            return 'Данная колонка не существует'
        if user[column] == val:
            print(user)
            flag = True
    if not flag:
        print('Данные не обнаружены')


file_base = 'database.csv'
