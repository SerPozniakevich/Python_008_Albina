import dataclasses
from input_data import add_contact, input_column
from contact_op import find_contact, get_columns, read_data, add_column, write_data


def user_interfase():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag:
        print('\nБАЗА ДАННЫХ\nВыберете пункт:')
        while True:
            print('1 - Поиск контакта')
            print('2 - Добавление контакта')
            print('3 - Показать справочник')
            print('4 - Добавить колонку')
            print('5 - Выход')
            choice = input()
            if choice not in ['1', '2', '3', '4', '5']:
                print('Повторите ввод команды')
                continue
            if choice == '1':
                find_contact(data)
            elif choice == '2':
                add_contact(data, columns)
            elif choice == '3':
                print(columns)
                print(data)
            elif choice == '4':
                column = input_column()
                data = add_column(data, column, columns)
            else:
                flag = False
                write_data(data, columns)
                break



if __name__ == "__main__": # __name__ - функция, запускающая функцию "напрямую" из данного файла, а не по импорту
    user_interfase()
