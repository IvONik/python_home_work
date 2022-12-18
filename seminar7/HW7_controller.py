from homework.seminar7 import HW7_view
from homework.seminar7 import HW7_midel
import logging
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,encoding='utf-8')

def main_function():
    try:
        select = HW7_view.greeting()
        logging.info('пользователь обратился за справочником')
        if select == 1:
            print('вы выбрали 1')
            HW7_midel.show_spravochnik_consol()
            logging.info('справочник выведен на экран')
        elif select == 2:
            print('вы выбрали 2, откройте файл')
            HW7_midel.writer_file()
            logging.info('справочник записан в файл')
    except Exception as err:
        print('введено некорректное значение')
        # HW7_midel.unkorrect_input()
        logging.warning("введено некорректное значение")

