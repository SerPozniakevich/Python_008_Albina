
def creat_csv():
    file_base = 'database.csv'
    with open (file_base, "w", encoding = 'UTF=8') as f:
        f.write(f'Фамилия, Имя,\n')
