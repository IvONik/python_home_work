#чтение  csv файла
#
# import csv
# with open('homework\seminar7\spravochnik.csv',encoding="utf8") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     title = next(reader) # эта строчка чтобы не записывать заголовок
#     sp = list(reader)
#     for row in sp:
#         print(row)
#
# #чтение  в словарь
#
# with open('homework\seminar7\spravochnik.csv',encoding="utf8") as csvfile:
#     reader = csv.Dictreader(csvfile, delimiter=',')
#     expensive = sorted(reader, key=lambda x:int(x['price'])
# for record in expensive:
#     print(record)
import csv

#запись в файл(для перезаписи, режим w)
# with open('file.csv', 'a', encoding='utf8', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     row =['колбаса', 500, 'микоян'] # строчка для добавления
#     writer.writerow(row)


# запись словаря в файл
data = [{
    'lastname':'Иванов',
     'firstname':'Петр',
    'class_number': 9
},{
    'lastname':'Кузнецов',
    'firstname':'Петр',
    'class_number': 9
}]
with open('dictwriter.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=',')#fildname-имена столбцов(берем нулевой элемент data по ключу
    writer.writeheader()#записали сохраненные заголовки
    for d in data:
        writer.writerow(d)