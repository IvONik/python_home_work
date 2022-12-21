import csv
list_spravochnik = [['Фамилия','Имя','Отчество','телефон'],
['Иванов','Иван','Иванович','2983485'],
['Иванов','Петр','Андреевич','23847873'],
['Иванов','Сергей','Анатольевич','4547545'],
['Петров','Вячеслав','Иванович','948454'],
['Смирнов','Кирилл','Николаевич','398434']]


def show_spravochnik_consol():
    list_spravochnik =[]
    with open("spravochnik.csv", encoding='utf-8') as file_read:
        data = csv.reader(file_read, delimiter = ",")
        for row in data:
            print(*row)
            list_spravochnik.append(row)


def writer_file():
    with open("spravochnik_record.txt", mode="w", encoding='utf-8') as file_record:
        file_writer = csv.writer(file_record, delimiter=",", lineterminator="\r")
        for row in list_spravochnik:
            file_writer.writerow(row)


# def unkorrect_input(select):
#     if select != 1 or select != 2:
#         print('введено некорректоное значение')

