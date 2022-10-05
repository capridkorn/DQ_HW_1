txt = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

txt_low = txt.lower()  # переводим все символы в нижний регистр


"""txt_n = ''
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
        txt_n += txt_low[i]  # Остальные слова добавляем без изменения"""


# Новая реализация
lst_n = txt_low.split('.')  # разделяем строку на список строк по разделителю "."
txt_n = ''  # создаем пустую строку куда будем записывать скорректированную строку
for i in range (len(lst_n)):  # цикл по каждой строке списка
    if i == 0:   # первую строку списка нужно дополнительно разделить
        a = lst_n[i].split(':')  # по разделителю ":"
        txt_n = a[0].strip().capitalize() + ':\n' + a[1].strip().capitalize()  # в заготовленную переменную записываем строки с заглавной буквы и удаленными лишними пробелами
    else:
        a = lst_n[i].strip().capitalize()  # удаляем лишние пробелы и делаем первую букву заглавной
        if i == len (lst_n)-1:  # это условие нужно чтобы не ставить в конце лишнюю точку
            txt_n += a  # в заготовленную переменную записываем строку
        else:
            txt_n += a + '.\n' # в заготовленную переменную записываем строки разделяя их точкой и переносом каретки
#print (txt_n)  # для дебага


txt_n_r = txt_n.replace(' iz', ' is')  # Заменяем iz на is если перед ним есть пробел
print('Текст в корректном виде: \n', txt_n_r)  # Выводим текст

txt_fnl = ''
lst = []
lst1 = []
lst = txt_n_r.split()  # Переводим текст в список
for i in lst:  # Проходим по списку
    if i[-1] == '.':  # Если у элемента есть точка в конце,
        lst1.append(i[:-1])  # тогда его записывааем в отдельный список (без точки)

txt_fnl = txt_n_r + '\n' + ' '.join(
    lst1) + '.'  # К основному тексту добавляем текст с последними словами каждого предложения
print('Текст в корректном виде с добавочным предложением: \n', txt_fnl)  # Выводим на экран

cnt = 0
for i in range(len(txt_fnl)):  # Проходим по тексту и считаем кол-во whitespace символов
    if txt_fnl[i] == ' ' or txt_fnl[i] == '\n' or txt_fnl[i] == '\t' or txt_fnl[i] == '\v' or txt_fnl[i] == '\r' or \
            txt_fnl[i] == '\f':
        cnt += 1
print('Количество whitespace символов в конечном тексте:', cnt)