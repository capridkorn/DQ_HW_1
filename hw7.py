import csv
import re


class WordCountToFile:  # Class for 'word-count' csv

    @staticmethod
    def words_from_file():  # Method to create list of items from file
        wrd_lst = []
        with open('newsfeed.txt', 'r') as file:  # Open file
            for line in file:  # For each line
                wrd_lst += line.lower().strip('\n').split(' ')  # Find items by space separator and make in lowercase
            return wrd_lst

    @staticmethod
    def clear_words(wrd_lst):  # Method to clean up the list so only words will remain
        wrd_lst_final = []
        for i in range(len(wrd_lst)):
            wrd_lst[i] = re.sub('[^A-Za-z]', '', wrd_lst[i])  # Replace all but letters with blanks (only words remain)
            if wrd_lst[i] == '---' \
                    or wrd_lst[i] == '-------------------------------------------------------------' \
                    or wrd_lst[i] == '----------------------------------------------------------------------' \
                    or wrd_lst[i] == '-------------------------------------------------------' \
                    or wrd_lst[i] == '----------------------------------------------' \
                    or wrd_lst[i] == '':
                continue
            else:
                wrd_lst_final.append(wrd_lst[i])  # Writing cleared word values to the list
        return wrd_lst_final

    @staticmethod
    def count_unique(wrd_lst_final):  # Method to create dictionary unique word-count
        dct = {}
        for i in range(len(wrd_lst_final)):
            dct[wrd_lst_final[i]] = 0  # Write unique words from the list to dictionary as keys with value 0
        for i in range(len(wrd_lst_final)):
            dct[wrd_lst_final[i]] += 1  # Count words in list and write it as value to dictionary
        return dct

    @staticmethod
    def write_to_file(dct):  # Method to rewrite the csv file with new data
        with open('word_num.csv', 'w') as csvfile:  # Open file
            for i in dct.keys():
                writer_csv = csv.writer(csvfile, delimiter='-')  # Set writer with delimiter '-'
                writer_csv.writerow([i, str(dct[i])])  # Write to each row key and value from dct


class LetterStatToFile:  # Class for 'letter, cout_all, count_uppercase, percentage' csv

    @staticmethod
    def letters_from_file():  # Method to create list of items from file
        ltr_lst = []
        with open('newsfeed.txt', 'r') as file:
            for line in file:
                ltr_lst += line.strip('\n')
            return ltr_lst

    @staticmethod
    def clear_letters(ltr_lst):  # Method to create list of letters from file
        ltr_lst_clr = []
        for i in range(len(ltr_lst)):
            if ltr_lst[i].isalpha():  # Write only letters
                ltr_lst_clr.append(ltr_lst[i])
        return ltr_lst_clr

    @staticmethod
    def count_unique_upper(ltr_lst_clr):  # Method to create dictionary with unique upper letters and count
        dct_upr = {}
        cnt_unq_upr = []
        for i in range(len(ltr_lst_clr)):
            if ltr_lst_clr[i].istitle():  # Add only letters that are in uppercase
                cnt_unq_upr.append(ltr_lst_clr[i])
        for i in range(len(cnt_unq_upr)):
            dct_upr[cnt_unq_upr[i]] = 0  # Write unique letter from the list to dictionary as keys with value 0
        for i in range(len(cnt_unq_upr)):
            dct_upr[cnt_unq_upr[i]] += 1  # Count letters in list and write it as value to dictionary
        return dct_upr

    @staticmethod
    def count_unique_all(ltr_lst_clr):  # Method for count all unique letters
        dct = {}
        ltr_lst_lwr = []
        for i in ltr_lst_clr:
            ltr_lst_lwr.append(i.lower())  # All letters to lowercase
        for i in range(len(ltr_lst_lwr)):
            dct[ltr_lst_lwr[i]] = 0  # Write unique letter from the list to dictionary as keys with value 0
        for i in range(len(ltr_lst_lwr)):
            dct[ltr_lst_lwr[i]] += 1  # Count letters in list and write it as value to dictionary
        return dct

    @staticmethod
    def count_all(unq_all):  # Method to count all letters
        cnt = 0
        for i in unq_all:
            cnt += unq_all[i]
        return cnt

    @staticmethod
    def write_to_file2(cnt_all, cnt_upr, cnt):  # Method to rewrite the csv file with new data
        with open('letter_num.csv', 'w') as csvfile:  # Open the file
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']  # Set up the headers
            writer = csv.DictWriter(csvfile, fieldnames=headers)  # Create writer and announce the headers
            writer.writeheader()  # Write headers to the file
            for i in cnt_all:
                if i.upper() in cnt_upr:
                    cnt_upr_v = cnt_upr[i.upper()]
                else:
                    cnt_upr_v = 0  # If there are no such letter in uppercase, write 0
                writer.writerow({'letter': i, 'count_all': cnt_all[i], 'count_uppercase': cnt_upr_v,
                                 'percentage': str(cnt_all[i] / cnt * 100) + '%'})
