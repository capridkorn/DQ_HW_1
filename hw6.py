from datetime import datetime, date  # Import 'datetime' module for working with datetime
import random  # Import 'random' module for random number generation
import os  # Import 'os' module for working with system files
import hw4  # Import methods from homework 4
import hw7  # Import methods from homework 7
import hw8_9  # Import methods from homework 8 and 9
#import sqlite3
import pyodbc


# Class General where various methods are located
class General:
    def __init__(self):
        self.a = 0

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

    def write_record_db(self, rec_txt, city, today, connection):  # hw10 Method for writing News record to the database
        cursor = connection.cursor()
        cursor.execute('create table if not exists News(Text, City, Current_Date)')
        cursor.execute("insert into News values ('"+rec_txt+"', '"+city+"', '"+today+"')")
        cursor.execute("select count(0) from News")
        n = cursor.fetchall()
        num = int(n[0][0])
        cursor.execute("select * from News")
        tbl = cursor.fetchall()
        fl = True
        for i in range(num-1):
            if tbl[num-1] != tbl[i]:
                continue
            elif tbl[num-1] == tbl[i]:
                fl = False
                break
        if fl:
            connection.commit()
        cursor.close()


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
    def write_record(rec_txt, date_to, days_left):  # Method for writing Private Ad record to the file
        f = open("newsfeed.txt", "a")
        f.write('--- PRIVATE AD -------------------------------------------------------\n')  # Write header to the file
        f.write(rec_txt + '\n')  # Write main text of the News record to the file
        f.write('Actual until: ' + str(date_to) + ', ' + days_left + '\n')  # Write Date_to and number of days left
        f.write('----------------------------------------------------------------------\n\n')  # Write footer to file
        f.close()  # File closing

    def write_record_db(self, rec_txt, date_to, days_left, connection):  # hw10 Method for writing Private Ad record to the database
        cursor = connection.cursor()
        cursor.execute('create table if not exists PrivateAd(Text, Actual_until, Days_left)')
        date_to = date_to.strftime("%Y-%m-%d")
        cursor.execute("insert into PrivateAd values ('"+rec_txt+"', '"+date_to+"', '"+days_left+"')")
        cursor.execute("select count(0) from PrivateAd")
        n = cursor.fetchall()
        num = int(n[0][0])
        cursor.execute("select * from PrivateAd")
        tbl = cursor.fetchall()
        fl = True
        for i in range(num - 1):
            if tbl[num - 1] != tbl[i]:
                continue
            elif tbl[num - 1] == tbl[i]:
                fl = False
                break
        if fl:
            connection.commit()
        cursor.close()


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
    def write_record(rec_txt, ans_txt, complexity):  # Method for writing Questions record to the file
        f = open("newsfeed.txt", "a")
        f.write('--- QUESTION OF THE DAY ----------------------------------------------\n')  # Write header to the file
        f.write(rec_txt + '\n')  # Write main text of the News record to the file
        f.write('Answer: ' + ans_txt + '\n')  # Write answer text of the News record to the file
        f.write('Complexity of the question: ' + str(complexity) + '/5\n')  # Write complexity to the file
        f.write('----------------------------------------------------------------------\n\n')  # Write footer to file
        f.close()  # File closing

    def write_record_db(self, rec_txt, ans_txt, complexity, connection):  # hw10 Method for writing Questions record to the database
        cursor = connection.cursor()
        complexity = str(complexity)
        cursor.execute('create table if not exists QuestionOfTheDay(Text, Answer, Complexity)')
        cursor.execute("insert into QuestionOfTheDay values ('"+rec_txt+"', '"+ans_txt+"', '"+complexity+"')")
        cursor.execute("select count(0) from QuestionOfTheDay")
        n = cursor.fetchall()
        num = int(n[0][0])
        cursor.execute("select * from QuestionOfTheDay")
        tbl = cursor.fetchall()
        fl = True
        for i in range(num - 1):
            if tbl[num - 1] != tbl[i]:
                continue
            elif tbl[num - 1] == tbl[i]:
                fl = False
                break
        if fl:
            connection.commit()
        cursor.close()


# Class for reading records from the file .txt
class FileOperationsTxt:
    def __init__(self):
        self.f_path = ''

    def input_file_path(self, frmt):  # Method for getting file path - standard or manually entered
        path_option = int(input('Please select where file for reading is located?\n1 - Standard path\n2 - I want to '
                                'enter path manually\nPlease enter selected option: '))
        if path_option == 1:
            if frmt == 1:  # Option for .txt
                self.f_path = 'readfile.txt'  # File is located in the same folder as .py - only name could be mentioned
            elif frmt == 2:  # Option for .json
                self.f_path = 'readfile.json'  # File is located in the same folder as .py - only name could be mentioned
            elif frmt == 3:  # Option for .xml
                self.f_path = 'readfile.xml'  # File is located in the same folder as .py - only name could be mentioned
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
                    News().write_record_db(rec_txt, city, today, con)  # For writing record to db we use existing method
                elif lst_line[0] == 'private ad':  # If type of record is 'Private Ad'
                    rec_txt = hw4.words_normalize_case(lst_line[1])  # Use imported function to normalize the text
                    date_str = lst_line[2]  # Date is taken from the part of the line
                    date_to = PrivateAd().str_to_date(date_str)  # For converting string to date we use existing method
                    days_left = PrivateAd().day_left_calculation(date_to)  # For calc days left we use existing method
                    PrivateAd().write_record_db(rec_txt, date_to, days_left, con)  # For writing record to db existing method is used
                    PrivateAd().write_record(rec_txt, date_to, days_left)  # For writing record existing method is used
                elif lst_line[0] == 'question of the day':  # If type of record is 'Question of the day'
                    rec_txt = hw4.words_normalize_case(lst_line[1])  # Use imported function to normalize the text
                    ans_txt = lst_line[2]  # Answer text is taken from the part of the line
                    complexity = Question().complexity()  # For random complexity we use existing method
                    Question().write_record(rec_txt, ans_txt, complexity)  # For writing record existing method is used
                    Question().write_record_db(rec_txt, ans_txt, complexity, con)  # For writing record to db existing method is used
                else:  # If file doesn't correspond to pattern
                    print('Error in input format')
                    break
        print('Input file was successfully processed.')


if __name__ == '__main__':
    # con = sqlite3.connect('results.db')  # Connection to the database
    con = pyodbc.connect('Driver={SQLite3 ODBC Driver};SERVER=localhost;Database=results.db;Trusted_connection=yes')
    g = General()
    gr = GeneralRecord()
    n = News()
    pa = PrivateAd()
    q = Question()
    fot = FileOperationsTxt()
    foj = hw8_9.FileOperations()
    print('Hello, dear editor. Please select how you want to add records:\n1 - Manually\n2 - Via File')
    enter_method = g.r_option()
    if enter_method == 1:
        print('Please select type of record you want to add:\n1 - News\n2 - Private Ad\n3 - Question of the day')
        record_type = g.r_option()
        if record_type == 1:
            txt = n.input_text()
            ct = n.input_city()
            dt = n.current_date()
            n.write_record(txt, ct, dt)
            n.write_record_db(txt, ct, dt, con)
            n.thanks()
        elif record_type == 2:
            txt = pa.input_text()
            dte = pa.date_insert()
            dt_to = pa.str_to_date(dte)
            dl = pa.day_left_calculation(dt_to)
            pa.write_record(txt, dt_to, dl)
            pa.write_record_db(txt, dt_to, dl, con)
            pa.thanks()
        elif record_type == 3:
            txt = q.input_text()
            ans = q.input_answer()
            cmp = q.complexity()
            q.write_record(txt, ans, cmp)
            q.write_record_db(txt, ans, cmp, con)
            q.thanks()
    elif enter_method == 2:
        print('Please select file format you want to use for data upload:\n1 - .txt\n2 - .json\n3 - .xml')
        format = g.r_option()
        if format == 1:
            fot.input_file_path(format)
            fot.read_file()
            fot.delete_file()
        elif format == 2:  # hw8
            foj.input_file_path(format)
            foj.read_file_json()
            foj.delete_file()
        elif format == 3:  # hw9
            foj.input_file_path(format)
            foj.read_file_xml()
            foj.delete_file()
    # hw7 part:
    wct = hw7.WordCountToFile
    wff = wct.words_from_file()
    cw = wct.clear_words(wff)
    cu = wct.count_unique(cw)
    wct.write_to_file(cu)
    lsf = hw7.LetterStatToFile
    lff = lsf.letters_from_file()
    cl = lsf.clear_letters(lff)
    cuu = lsf.count_unique_upper(cl)
    cua = lsf.count_unique_all(cl)
    ca = lsf.count_all(cua)
    lsf.write_to_file2(cua, cuu, ca)
    con.close()