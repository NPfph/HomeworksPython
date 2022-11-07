import staff_info as si
import info_departments as di


def option():
    print("\nПрограмма мониторинга сотрудников")
    choice = int(input('Поиск информации: \n \
    1: Информация о сотруднике по фамилии \n \
    2: Посмотреть расположение отдела сотрудника \n \
    3: Выход\n \
    Ваш выбор: '))

    if choice == 1:
        Surn = str(input("Введите фамилию сотрудника: "))
        if Surn in si.emp_card['Фамилия']:
            index = si.emp_card['Фамилия'].index(Surn)
        print(f"{si.emp_card['ID'][index]}{si.emp_card['Имя'][index]}{si.emp_card['Фамилия'][index]}{si.emp_card['Дата рождения'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

option()
