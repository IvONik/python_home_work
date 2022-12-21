def show_menu():
    print('выберите действия: \n'
          '1 - вывести список сотрудников, 2- добавить сотрудника,\n'
          '3 - изменить данные сотрудника, 4-удалить сотрудника\n'
          '5 - импортировать файл,         6 - записать файл')
    try:
        select = int(input())
        if not select in [1,2,3,4,5,6]:
            raise ValueError
        return select
    except Exception:
        print('все пропало')
        exit()

def show_employers(spisok):
    for i, sotrudnik in enumerate(spisok):
        if i ==0:
            print('', *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employers():
    print('Введите должность, ФИО через пробел')
    data = input().split()
    return data


def change_employer():
    print('выберите строку для перезаписи:')
    number = int(input())
    print('введит строку')
    string = input().split()
    return number,string #вернет картеж


def delete():
    print('введите номер строки для удаления')
    number = int(input())
    return number