import json
import xml.etree.ElementTree as ET
import hw6


# Class for reading records from the file
class FileOperations(hw6.FileOperationsTxt):
    def __init__(self):
        self.f_path = ''

    def read_file_json(self):  # Method for reading json file
        json_file = json.load(open(self.f_path))
        records = json_file["records"]
        for i in records:
            if i["type"] == 'news':  # If type of record is 'News'
                rec_txt = i["text"]  # Text is taken from 'text' key
                city = i["city"]  # City is taken from 'city' key
                today = hw6.News().current_date()  # For taking current date we use already existing method
                hw6.News().write_record(rec_txt, city, today)  # For writing record to the file we use existing method
            elif i["type"] == 'private ad':  # If type of record is 'Private Ad'
                rec_txt = i["text"]  # Text is taken from 'text' key
                date_str = i["date_to"]  # Date is taken from 'date' key
                date_to = hw6.PrivateAd().str_to_date(date_str)  # For converting string to date we use existing method
                days_left = hw6.PrivateAd().day_left_calculation(date_to)  # For calc days left we use existing method
                hw6.PrivateAd().write_record(rec_txt, date_to, days_left)  # For writing record existing method is used
            elif i["type"] == 'question of the day':  # If type of record is 'Question of the day'
                rec_txt = i["text"]  # Text is taken from 'text' key
                ans_txt = i["answer"]  # Answer is taken from 'answer' key
                complexity = hw6.Question().complexity()  # For random complexity we use existing method
                hw6.Question().write_record(rec_txt, ans_txt, complexity)  # For writing record existing method is used
            else:  # If file doesn't correspond to pattern
                print('Error in input format')
                break

    # hw9
    def read_file_xml(self):  # Method for reading xml file
        xml_file = ET.parse(self.f_path)
        records = xml_file.getroot()

        for i in records:
            if i.attrib['name'] == 'news':  # If type of record is 'News'
                for j in i:
                    if j.tag == 'text':
                        rec_txt = j.text
                    if j.tag == 'city':
                        city = j.text
                today = hw6.News().current_date()  # For taking current date we use already existing method
                hw6.News().write_record(rec_txt, city, today)  # For writing record to the file we use existing method
            elif i.attrib['name'] == 'private ad':  # If type of record is 'Private Ad'
                for j in i:
                    if j.tag == 'text':
                        rec_txt = j.text
                    if j.tag == 'date_to':
                        date_str = j.text
                        date_to = hw6.PrivateAd().str_to_date(date_str)  # For converting string to date we use existing method
                        days_left = hw6.PrivateAd().day_left_calculation(date_to)  # For calc days left we use existing method
                hw6.PrivateAd().write_record(rec_txt, date_to, days_left)  # For writing record existing method is used
            elif i.attrib['name'] == 'question of the day':  # If type of record is 'Question of the day'
                for j in i:
                    if j.tag == 'text':
                        rec_txt = j.text
                    if j.tag == 'answer':
                        ans_txt = j.text
                complexity = hw6.Question().complexity()  # For random complexity we use existing method
                hw6.Question().write_record(rec_txt, ans_txt, complexity)  # For writing record existing method is used
            else:  # If file doesn't correspond to pattern
                print('Error in input format')
                break