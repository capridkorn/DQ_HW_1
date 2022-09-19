import random  # импортирует модуль random
from decimal import Decimal  # импортирует модуль decimal

new_list = []  # объявляем пустой список

# заполняем список рандомными числами
for i in range (100):  # создаем цикл от 0 до 100
    rnd = random.randint(0, 1000)  # используем метод randint для генерации случайного числа от 0 до 1000
    new_list.append(rnd)  # используем метод добавления в список сгенерированного ранее случайного числа
    i += 1  # шаг инкремента

# print (new_list)

# Сортировка пузырьком
for i in range(len(new_list)-1):  # проходим по всем элементам списка
    for j in range (len(new_list)-i-1):  # для каждого элемента списка проходим по элементам списка. при каждой итерации элементов становится на 1 меньше, так как в конце фиксируются уже отсортированные элементы
        if new_list[j] > new_list[j+1]:  # Сравниваем выбранный элемент списка со следующим
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # Если выбранный элемент спискаа больше, то меняем элементы местами (больший двигаем к концу)

# print (new_list)

avg_even = Decimal(0)  #объявляем переменную для среднего четных чисел
avg_odd = Decimal(0)  #объявляем переменную для среднего неченых чисел
cnt_even = 0  #объявляем переменную для счетчика четных чисел
cnt_odd = 0  #объявляем переменную для счетчика нечетных чисел

# вычисляем среднее значение
for i in new_list: #берем каждый элемент из списка
    if i % 2 == 0:  # по остатку определяем четное
        avg_even += i  # добавляем значение элемента в переменную
        cnt_even += 1  # подсчитываем сколько было записано четных элементов
    else:  # и нечетное
        avg_odd += i  # добавляем значение элемента в переменную
        cnt_odd += 1  # подсчитываем сколько было записано нечетных элементов

avg_even = avg_even/cnt_even  # считаем среднее для четных
avg_odd = avg_odd/cnt_odd  # считаем среднее для нечетных

print('Среднее зничение четных элементов списка: ', avg_even)  # вывод среднего значения для четных элементов списка
print('Среднее зничение нечетных элементов списка: ', avg_odd)  # вывод среднего значения для нечетных элементов списка
