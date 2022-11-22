


def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    desc = input("Введите описание контакта: ")
    return [last_name, first_name, brith_name, phone_number, desc]

def choice():
    print('Выберите команду:\n 1 - Экспорт данных \n 2 - Импорт данных \n 3 - Поиск контакта')
    cho = input('Введите цифру: ')
    if cho == 1:
        