import random  # импортирует модуль random
import string  # импортирует модуль string

# hw2
# Функция создает список и заполняет его пустыми словарями
def new_empty_list():
    lst = []  # объявляем пустой список
    # заполняем список случайным (от 2 до 10) количеством пустых словарей:
    for i in range(random.randint(2, 10)):  # выбираем случайное чило от 2 до 10
        lst.append({})  # и такое количество раз добавляем в список пустой словарь
    return lst

# Функция для заполнения словарей в списке случайным количеством значений
def fill_dct_in_list(t):
    for dct_n in range(len(t)):  # цикл проходит по каждому словарю в списке
        for i in range(random.randint(2, 10)):  # цикл проходит по каждому значению словаря, создавая их в количестве от 2 до 10
            kn = {random.choice(string.ascii_lowercase):random.randint(1,100)}  # заполняем значение словаря случайной парой буква/число
            t[dct_n].update(kn)  # пара ключ/значение добавлятся в целевой словарь
    return t

# Функция для создания списка, в который будут записаны и отсортировааны ключи
def keys_list(t):
    ks = []  # объявление пустого списка, куда будут записаны ключи со всех словарей
    for i in range (len(t)):  # цикл прохождения по словарям в списке
        ks = ks + list(t[i].keys())  # в пустой список записываются ключи с каждого списка
    ks.sort()  # сортируем список
    #print('Ключи со всех словарей:', ks)  # вывести список всех ключей для дебага
    return ks

# Функция, которая убирает дубликаты из списка ключей
def keys_unique_list(t):
    ks_n = []  # объявляем пустой список, куда запишем ключи со всех словарей без дубликатов
    for i in range(len(t)):  # проходим по списку ключей со всех словарей
        if i == len(t) - 1:  # условие на последний элемент списка
            ks_n += t[i]  # записываем в переменную
        elif t[i] == t[i + 1]:  # если элемент равен следующему
            continue  # ничего не делаем
        elif t[i] != t[i + 1]:  # если элемент не равен следующему
            ks_n += t[i]  # записываем в переменную
    # print('Уникальные ключи:', ks_n)  # вывести список уникальных ключей для дебага
    return ks_n

# Функция, которая формирует финальный словарь по условиям задачи
def final_list(a, b):
    key_in_dicts = []  # объявляем пустой список, куда запишем значения по ключу
    k_name = ''  # объявляем переменную string в которую запишем скорректированное название ключа
    st_lst = []  # объявляем пустой список, куда запишем пары ключ/макс значение
    fnl_lst = []  # объявляем пустой список, куда запишем финальный результат
    for i in range(len(b)):  # проходим по каждому уникальному ключу
        for j in range(len(a)):  # проходим по каждому словарю для выбранного ключа
            key_in_dicts.append(a[j].get(b[i]))  # записываем значения по ключу в список
        #print(key_in_dicts)  # вывести значения по ключу для дебага
        key_in_dicts_wo_null = [] # объявляем пустой список, куда запишем значения по ключу без значения None
        for k in key_in_dicts:  # проходим списку значений по ключу
            if k != None:
                key_in_dicts_wo_null.append(k) # записываем только значения не равные None
        #print(key_in_dicts_wo_null)  # вывести значения по ключу без значения None для дебага
        if len(key_in_dicts_wo_null) > 1:  # если значений одного ключа больше чем одно - значит нужно менять название ключа
            k_name = b[i]+'_'+str(key_in_dicts.index(max(key_in_dicts_wo_null)))  # формируем новое назваание ключа добавляя нижнее подчеркивание и порядковый номер словаря, где находится его макс значение
            st_lst.append(k_name)  # в переменную записываем сформированное имя
            st_lst.append(max(key_in_dicts_wo_null))  # в переменную записываем максимальное значение
            st_lst_t = tuple(st_lst)  # переводим в тип tuple чтобы потом сформировать dict
        elif len(key_in_dicts_wo_null) == 1:  # если значений одного ключа больше одно - значит менять название ключа не нужно
            st_lst.append(gks_n[i])  # в переменную записываем название ключа
            st_lst.append(max(key_in_dicts_wo_null))  # в переменную записываем значение
            st_lst_t = tuple(st_lst)  # переводим в тип tuple чтобы потом сформировать dict
        #print(st_lst_t)  # выводим новое имя ключа + значение для дебага
        key_in_dicts.clear()  # очищаем список перед след циклом
        fnl_lst.append(st_lst_t)  # добавляем значение в финальную переменную
        st_lst.clear() # очищаем список перед след циклом
    fnl_lst = dict(fnl_lst)  # переводим в словарь
    return fnl_lst


# hw3
txt = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Функция, которая делает нормализацию букв с точки зрения регистра
def words_normalize_case(t):
    txt_low = txt.lower()  # переводим все символы в нижний регистр
    txt_n = ''
    for i in range(len(txt_low)):  # проходим по каждому элементу списка
        if i == 0:  # Первое слово текста пишем с большой буквы
            txt_n += txt_low[i].upper()
        elif txt_low[i - 1] == ' ' and txt_low[i - 2] == ' ' and txt_low[i - 3] == '\n' and txt_low[i - 4] == ' ' and \
                txt_low[i - 5] == '\n' and txt_low[i - 6] == '.':
            txt_n += txt_low[i].upper()  # Слово после точки с новой строки - с большой буквы
        elif txt_low[i - 1] == ' ' and txt_low[i - 2] == ' ' and txt_low[i - 3] == '\n' and txt_low[i - 4] == ':':
            txt_n += txt_low[i].upper()  # Слово после двоеточия с новой строки - с большой буквы (по контексту)
        elif txt_low[i - 1] == ' ' and txt_low[i - 2] == '.':  # Слово после точки в той же строке - с большой буквы
            txt_n += txt_low[i].upper()
        else:
            txt_n += txt_low[i]  # Остальные слова добавляем без изменения
    return txt_n

# Функция, которая заменяет iz на is
def iz_to_is(t):
    txt_n_r = gtxt_n.replace(' iz', ' is')  # Заменяем iz на is если перед ним есть пробел
    return txt_n_r

# Функция, которая генерирует и добавяет доп текст
def add_sentence(t):
    txt_fnl = ''
    lst = []
    lst1 = []
    lst = gtxt_n_r.split()  # Переводим текст в список
    for i in lst:  # Проходим по списку
        if i[-1] == '.':  # Если у элемента есть точка в конце,
            lst1.append(i[:-1])  # тогда его записываем в отдельный список (без точки)
    txt_fnl = gtxt_n_r + '\n' + ' '.join(
        lst1) + '.'  # К основному тексту добавляем текст с последними словами каждого предложения
    return txt_fnl

# Функция которая считает количество whitespace символов
def cnt_whitespases(t):
    cnt = 0
    for i in range(len(t)):  # Проходим по тексту и считаем кол-во whitespace символов
        if t[i] == ' ' or t[i] == '\n' or t[i] == '\t' or t[i] == '\v' or t[i] == '\r' or t[i] == '\f':
            cnt += 1
    return cnt





##################
###### main ######
##################

# hw2
lst = new_empty_list()  # Создание списка и заполнение его пустыми словарями
glst = fill_dct_in_list(lst)  # Заполнение словарей в списке случайным количеством значений
print('Сгенерированный список словарей:', glst)
gks = keys_list(glst)  # Создание списка, в который будут записаны и отсортировааны ключи
gks_n = keys_unique_list(gks)  # Удаление дубликатов из списка ключей
fnl_lst = final_list(lst, gks_n)  # Формирование финального словаря по условиям задачи
print ('Словарь сформированный по заданию:', fnl_lst)  #выводим сформированный словарь на экран

# hw3
gtxt_n = words_normalize_case(txt)  # Нормализация букв с точки зрения регистра
gtxt_n_r = iz_to_is(gtxt_n)  # Замена iz на is
print('Текст в корректном виде: \n', gtxt_n_r)  # Выводим текст
gtxt_fnl = add_sentence(gtxt_n_r)  # Добавление дополнительного предложения
print('Текст в корректном виде с добавочным предложением: \n', gtxt_fnl)  # Выводим на экран
f_cnt = cnt_whitespases(gtxt_fnl)  # Подсчет whitespace символов
print('Количество whitespace символов в конечном тексте:', f_cnt)