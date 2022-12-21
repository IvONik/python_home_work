import seminar8_view
import seminar8_model
import logging
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding='utf-8')

def main():
    select = seminar8_view.show_menu()
    if select == 1:
        logging.info('выбран пункт "Вывести список сотрудников"')
        sotr = seminar8_model.show_employers()
        seminar8_view.show_employers(sotr)
        logging.info('результат получен')
    elif select == 2:
        logging.info('выбран пункт "Добавить сотрудника"')
        data = seminar8_view.add_employers()
        seminar8_model.add_emloyer_to_list(data)
        logging.info('результат получен')
    elif select == 3:
        logging.info('выбран пункт "Изменить данные сотрудника"')
        change,string = seminar8_view.change_employer()
        seminar8_model.update_employers(change, string)
        logging.info('результат получен')
    elif select == 4:
        logging.info('выбран пункт "Удалить сотрудника"')
        number = seminar8_view.delete()
        seminar8_model.delete(number)
        logging.info('результат получен')
    elif select == 5:
        logging.info('выбран пункт "Импортировать файл"')
        seminar8_model.import_file()
        logging.info('результат получен')
    elif select == 6:
        logging.info('выбран пункт "Экспортировать файл"')
        seminar8_model.export_file()
        logging.info('результат получен')
    else:
        print('неизвестная команда')
        logging.info('неизвестная команда')
