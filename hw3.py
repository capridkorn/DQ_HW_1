txt = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.
 
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
 
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
 
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

txt_low = txt.lower()  # переводим все символы в нижний регистр

txt_n = ''
for i in range (len(txt_low)):  # проходим по каждому элементу списка
    if i == 0:  # Первое слово текста пишем с большой буквы
        txt_n += txt_low[i].upper()
    elif txt_low[i-1] == ' ' and txt_low[i-2] == ' ' and txt_low[i-3] == '\n' and txt_low[i-4] == ' ' and txt_low[i-5] == '\n' and txt_low[i-6] == '.':
        txt_n += txt_low[i].upper()  # Слово после точки с новой строки - с большой буквы
    elif txt_low[i-1] == ' ' and txt_low[i-2] == ' ' and txt_low[i-3] == '\n' and txt_low[i-4] == ':':
        txt_n += txt_low[i].upper() # Слово после двоеточия с новой строки - с большой буквы (по контексту)
    elif txt_low[i-1] == ' ' and txt_low[i-2] == '.':  # Слово после точки в той же строке - с большой буквы
        txt_n += txt_low[i].upper()
    else:
        txt_n += txt_low[i]  # Остальные слова добавляем без изменения

txt_n_r = txt_n.replace(' iz', ' is')   # Заменяем iz на is если перед ним есть пробел
print ('Текст в корректном виде: \n', txt_n_r)  # Выводим текст



txt_fnl = ''
lst = []
lst1 = []
lst = txt_n_r.split()  # Переводим текст в список
for i in lst:  # Проходим по списку
    if i[-1] == '.':  # Если у элемента есть точка в конце,
        lst1.append(i[:-1])  # тогда его записывааем в отдельный список (без точки)

txt_fnl = txt_n_r + '\n' + ' '.join(lst1) + '.'  # К основному тексту добавляем текст с последними словами каждого предложения
print ('Текст в корректном виде с добавочным предложением: \n', txt_fnl)   # Выводим на экран


cnt = 0
for i in range (len(txt_fnl)):  # Проходим по тексту и считаем кол-во whitespace символов
    if txt_fnl[i] == ' ' or txt_fnl[i] == '\n' or txt_fnl[i] == '\t' or txt_fnl[i] == '\v' or txt_fnl[i] == '\r' or txt_fnl[i] == '\f':
        cnt += 1
print('Количество whitespace символов в конечном тексте:' ,cnt)
