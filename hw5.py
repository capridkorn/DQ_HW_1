import datetime  # Импортируем модуль datetime для работы с временем
import random  # Импортируем модуль random

f = open("newsfeed.txt", "a")  # Открываем файл и указываем, что запись будет добавляться после последней.

class General:  # Класс General для описания общих методов.
    def __init__(self):
        self.a = 0

    def greetings(self):  # Метод для выведения приветственной записи
        print('Hello, dear editor. Please select type of record you want to add:\n1 - News\n2 - Advertisement\n3 - Question of the day')

    def input_option(self):  # Метод для считывания выбранной опции
        self.a = int(input('Please enter selected option: '))
        return self.a


class GeneralRecord:   # Родительский класс для описания общих метадов для всех видов заметок
    def __init__(self):
        self.txt = ''

    def input_text(self):  # Метод для считывания основного текста заметки
        self.txt = str(input('Please enter text for the record: ')) + '\n'
        return self.txt

    def thanks(self):  # Метод для выведения благодарственной записи
        print('Thank you. Record was added to the newsfeed. Have a nice day!')


class News(GeneralRecord):  # Класс для методов заметок типа News
    def __init__(self):
        self.today = ''
        self.dlft = ''
        self.ct = ''

    def input_city(self):   # Метод для считывания города
        self.ct = str(input('Please enter the city name: '))
        return self.ct

    def dt(self):  # Метод для определения даты
        self.today = datetime.datetime.now()  # Используем функцию datetime для работы с датой/временем
        self.today = self.today.strftime("%Y-%m-%d %H:%M")  # Переводим дату/время в строку нужного формата
        return (self.today)

    def write_record(self):  # Метод для записи новой строки в файл
        f.write('--- NEWS -------------------------------------------------------------\n')  # заголовок
        f.write(self.txt)  # основной текст
        f.write(self.ct + ', ' + self.today + '\n')  # город и дата/время
        f.write('----------------------------------------------------------------------\n\n')  # закрывающая строка


class PrivateAd(GeneralRecord):  # Класс для методов заметок типа PrivateAd
    def __init__(self):
        self.today = ''
        self.dlft = ''
        self.ds = ''

    def date_insert(self):  # Метод для считывания и преобразования даты
        print('Please enter expire date separately by YEAR, MONTH and DAY:')
        year = int(input('Please enter a year: '))
        month = int(input('Please enter a month: '))
        day = int(input('Please enter a day: '))
        self.dlft = datetime.date(year, month, day)
        return (self.dlft)

    def day_left_calculation(self): # Метод для расчета кол-ва дней которые остались
        self.today = datetime.date.today()
        self.ds = self.dlft - self.today  # отнимаем конечную дату от текущей
        if self.ds == 1:
            self.ds = str(self.ds.days) + ' day left'  # для одиночного окончания
        else:
            self.ds = str(self.ds.days) + ' days left'  # для множественного окончания
        return self.ds

    def write_record(self):  # Метод для записи новой строки в файл
        f.write('--- PRIVATE AD -------------------------------------------------------\n')  # заголовок
        f.write(self.txt)  # основной текст
        f.write('Actual until: ' + str(self.dlft) + ', ' + self.ds + '\n')  # Действует до
        f.write('----------------------------------------------------------------------\n\n')  # закрывающая строка


class Question(GeneralRecord):  # Класс для методов заметок типа Question
    def __init__(self):
        self.ans = ''
        self.cmp = 0

    def input_answer(self):  # Метод для считывания ответа
        self.ans = str(input('Please enter answer for the question: ')) + '\n'
        return self.ans

    def complexity(self):  # Метод рандомного выбора цифры сложности
        self.cmp = random.randint(1, 5)
        return self.cmp

    def write_record(self):  # Метод для записи новой строки в файл
        f.write('--- QUESTION OF THE DAY ----------------------------------------------\n')  # заголовок
        f.write(self.txt)  # основной текст
        f.write('Answer: ' + self.ans)  # ответ
        f.write('Complexity of the question: ' + str(self.cmp) + '/5\n')  # сложность
        f.write('----------------------------------------------------------------------\n\n')  # закрывающая строка


class Run:  # Класс для объявления всех остальных класов и запуска всех методов
    g = General()
    gr = GeneralRecord()
    n = News()
    pa = PrivateAd()
    q = Question()
    g.greetings()
    g.input_option()
    if g.a == 1:
        n.input_text()
        n.input_city()
        n.dt()
        n.write_record()
        n.thanks()
    elif g.a == 2:
        pa.input_text()
        pa.date_insert()
        pa.day_left_calculation()
        pa.write_record()
        pa.thanks()
    elif g.a == 3:
        q.input_text()
        q.input_answer()
        q.complexity()
        q.write_record()
        q.thanks()
    f.close()


if __name__ == '__main__':
    r = Run()  # основное объявление класса для запуска программы.

