import csv
list_sotrudniki = [{'должность': 'инженер', ' фамилия': ' Иванов', ' имя': ' Иван', ' телефон': 353434},
                   {'должность': 'методист', ' фамилия': 'Иванов', ' имя': 'Иван', ' телефон': 3587}]


def show_employers():
    with open('sotrudniki.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #title = next(reader) # эта строчка чтобы не записывать заголовок
        return list(reader)


def add_emloyer_to_list(data):
    with open('sotrudniki.csv', 'a', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)




def update_employers(number,string):
    try:
        with open('sotrudniki.csv', 'r', encoding='utf8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            data = list(reader)
            data[number] = string
        with open('sotrudniki.csv', 'w', encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for i in data:
                writer.writerow(i)
    except IndexError:# ошибки индекса
        print(' вы вышли за границы списка')
        exit()
    except Exception:# отлавливает другие ошибки
        print('появились другие ошибки')
        exit()


def delete(number):
    with open('sotrudniki.csv', 'r', encoding='utf8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        del data[number]
    with open('sotrudniki.csv', 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in data:
            writer.writerow(i)


def import_file():
    with open('sotrudniki.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        row = list(reader)
    for i in row:
        print(i)


def export_file():
    with open('sotrudniki_export.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(list_sotrudniki[0].keys()), delimiter=',')
        writer.writeheader()#записали сохраненные заголовки
        for l in list_sotrudniki:
            writer.writerow(l)


