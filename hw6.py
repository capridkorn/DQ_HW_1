from datetime import datetime, date  # Import 'datetime' module for working with datetime
import random  # Import 'random' module for random number generation
import os  # Import 'os' module for working with system files
import hw4  # Import methods from homework 4


# Class General where various methods are located
class General:
    def __init__(self):
        self.a = 0

    # def p_greetings(self):  # Method for showing welcome inscription
    #     print('Hello, dear editor. Please select how you want to add records:\n1 - Manually\n2 - Via File')
    #
    # def p_option_selection(self):
    #     print('Please select type of record you want to add:\n1 - News\n2 - Advertisement\n3 - Question of the day')

    def r_option(self):  # Method for user's input
        self.a = int(input('Please enter selected option: '))
        return self.a


# Parent class where general methods for working with different kind of notes are located
class GeneralRecord:

    @staticmethod
    def input_text():  # Method for input main text of the record
        rec_txt = str(input('Please enter text for the record: '))
        return rec_txt

    @staticmethod
    def thanks():  # Method for printing on screen 'thank you' record
        print('Thank you. Record was added to the newsfeed. Have a nice day!')


# Class where methods for working with News records are located
class News(GeneralRecord):

    def __init__(self):
        self.file_path = 'newsfeed.txt'  # variable with path to the file

    @staticmethod
    def input_city():   # Method for input city for record News
        city = str(input('Please enter the city name: '))
        return city

    @staticmethod
    def current_date():  # Method for obtaining today date
        today = datetime.now()  # By using datetime.now function we are getting today date
        today = today.strftime("%Y-%m-%d %H:%M")  # Convert datetype to string
        return today

    def write_record(self, rec_txt, city, today):  # Method for writing News record to the file
        f = open(self.file_path, "a")
        f.write('--- NEWS -------------------------------------------------------------\n')  # Write header to the file
        f.write(rec_txt + '\n')  # Write main text of the News record to the file
        f.write(city + ', ' + today + '\n')  # Write city and current date in one row to the file
        f.write('----------------------------------------------------------------------\n\n')  # Write footer to file
        f.close()  # File closing


# Class where methods for working with Private Ad records are located
class PrivateAd(GeneralRecord):  # Class PrivateAd has parent class GeneralRecord

    @staticmethod
    def date_insert():  # Method for date input
        date_str = input('Please enter expire date in a format: YEAR-MONTH-DAY: ')
        return date_str

    @staticmethod
    def str_to_date(date_str):  # Method for converting string to date
        date_to = datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_to

    @staticmethod
    def day_left_calculation(date_to):  # Method for counting days left
        today = date.today()
        ds = date_to - today  # To get days left subtracting the current date from the date_to
        if ds == 1:
            ds = str(ds.days) + ' day left'  # for singular ending
        else:
            ds = str(ds.days) + ' days left'  # 's ending for plural
        return ds

    @staticmethod
    def write_record(rec_txt, date_to, days_left):  # Method for writing News record to the file
        f = open("newsfeed.txt", "a")
        f.write('--- PRIVATE AD -------------------------------------------------------\n')  # Write header to the file
        f.write(rec_txt + '\n')  # Write main text of the News record to the file
        f.write('Actual until: ' + str(date_to) + ', ' + days_left + '\n')  # Write Date_to and number of days left
        f.write('----------------------------------------------------------------------\n\n')  # Write footer to file
        f.close()  # File closing


# Class where methods for working with Question records are located
class Question(GeneralRecord):

    @staticmethod
    def input_answer():  # Method for input text for answer of the record
        ans_txt = str(input('Please enter answer for the question: '))
        return ans_txt

    @staticmethod
    def complexity():  # Method for selecting random number
        complexity = random.randint(1, 5)  # Select random number from 1 to 5
        return complexity

    @staticmethod
    def write_record(rec_txt, ans_txt, complexity):  # Method for writing News record to the file
        f = open("newsfeed.txt", "a")
        f.write('--- QUESTION OF THE DAY ----------------------------------------------\n')  # Write header to the file
        f.write(rec_txt + '\n')  # Write main text of the News record to the file
        f.write('Answer: ' + ans_txt + '\n')  # Write answer text of the News record to the file
        f.write('Complexity of the question: ' + str(complexity) + '/5\n')  # Write complexity to the file
        f.write('----------------------------------------------------------------------\n\n')  # Write footer to file
        f.close()  # File closing


# Class for reading records from the file
class FileOperations:
    def __init__(self):
        self.f_path = ''

    def input_file_path(self):  # Method for getting file path - standard or manually entered
        path_option = int(input('Please select where file for reading is located?\n1 - Standard path\n2 - I want to '
                                'enter path manually\nPlease enter selected option: '))
        if path_option == 1:
            self.f_path = 'readfile.txt'  # File is located in the same folder as .py - only name could be mentioned
        elif path_option == 2:
            self.f_path = input('Please enter file path: ')  # Full path should be entered
        return self.f_path

    def delete_file(self):  # Method for removing file from the directory
        os.remove(self.f_path)  # Remove file from the directory (os function)

    def read_file(self):  # Method for reading file
        with open(self.f_path, 'r') as f:  # File opens for READ
            for line in f:  # Go through each line
                lst_line = line.strip('\n').split(' | ')  # Make list from line separating by |
                if lst_line[0] == 'news':  # If type of record is 'News'
                    rec_txt = hw4.words_normalize_case(lst_line[1])  # Use imported function to normalize the text
                    city = lst_line[2]  # City is taken from the part of the line
                    today = News().current_date()  # For taking current date we use already existing method
                    News().write_record(rec_txt, city, today)  # For writing record to the file we use existing method
                elif lst_line[0] == 'private ad':  # If type of record is 'Private Ad'
                    rec_txt = hw4.words_normalize_case(lst_line[1])  # Use imported function to normalize the text
                    date_str = lst_line[2]  # Date is taken from the part of the line
                    date_to = PrivateAd().str_to_date(date_str)  # For converting string to date we use existing method
                    days_left = PrivateAd().day_left_calculation(date_to)  # For calc days left we use existing method
                    PrivateAd().write_record(rec_txt, date_to, days_left)  # For writing record existing method is used
                elif lst_line[0] == 'question of the day':  # If type of record is 'Question of the day'
                    rec_txt = hw4.words_normalize_case(lst_line[1])  # Use imported function to normalize the text
                    ans_txt = lst_line[2]  # Answer text is taken from the part of the line
                    complexity = Question().complexity()  # For random complexity we use existing method
                    Question().write_record(rec_txt, ans_txt, complexity)  # For writing record existing method is used
                else:  # If file doesn't correspond to pattern
                    print('Error in input format')
                    break
        print('Input file was successfully processed.')


if __name__ == '__main__':
    g = General()
    gr = GeneralRecord()
    n = News()
    pa = PrivateAd()
    q = Question()
    fo = FileOperations()
    print('Hello, dear editor. Please select how you want to add records:\n1 - Manually\n2 - Via File')
    g.r_option()
    if g.a == 1:
        print('Please select type of record you want to add:\n1 - News\n2 - Private Ad\n3 - Question of the day')
        g.r_option()
        if g.a == 1:
            txt = n.input_text()
            ct = n.input_city()
            dt = n.current_date()
            n.write_record(txt, ct, dt)
            n.thanks()
        elif g.a == 2:
            txt = pa.input_text()
            dte = pa.date_insert()
            dt_to = pa.str_to_date(dte)
            dl = pa.day_left_calculation(dt_to)
            pa.write_record(txt, dt_to, dl)
            pa.thanks()
        elif g.a == 3:
            txt = q.input_text()
            ans = q.input_answer()
            cmp = q.complexity()
            q.write_record(txt, ans, cmp)
            q.thanks()
    elif g.a == 2:
        fo.input_file_path()
        fo.read_file()
        fo.delete_file()


'''
Список вопросов: 
1.  В классе General были принты, которые лежали по отдельным методам строка 12-16 (сейчас закомментированы). 
    Я их вынес в main. Корректно ли это?
2.  В классе Genaral остался один метод. То есть как будто класс ради класса. 
    Но в другие классы его вроде как нелогично добавлять по смыслу. Что с ним делать в таком случае? 
3.  Основной мой вопрос заключается в том, что я по сути ни в одном классе могу не использовать init секцию, 
    так как ничего не передаю в класс. И питон мне подсказывает, что все методы нужно сделать статическими. 
    Как то это все выглядит не так как нужно :(
4.  Oк ли вызывать методы из другого класса? Или тоже ужно это как-то по другому обыгрывать? например, строка 143
'''