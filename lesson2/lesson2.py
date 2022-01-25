# Встроенные типы и операции с ними

# Тип данных: число.
# В Python доступны следующие виды чисел: целые (тип int),
# вещественные (тип float),
# комплексные (тип complex).

i1 = 10
i2 = 11
i3 = i1 + i2

j1 = 10.0
j2 = 11
j3 = j1 + j2

# Тип данных: строка
# Строка в Python — упорядоченный набор символов для хранения и представления текстовой информации.

# Конкатенация (сцепление)


sql = """
 select * from DB 
 """

st1 = 'мама мыла раму!'
st2 = "папа мыл раму"
s = ' '
st3 = st1 + s + st2
s = '*'
st5 = s * 10

# Преобразование строк

print(len("my_string"))  # 9
print("раз два три".split())  # ['раз', 'два', 'три’]
print("четыре_пять_шесть".split('_'))  # ['четыре', 'пять', 'шесть']
print(' '.join(['раз', 'два', 'три']))  # ‘раз два три’
print(''.join(['раз', 'два', 'три']))  # раздватри
print("ехал грека через реку".title())  # Ехал Грека Через Реку
print('простая строка'.upper())  # ПРОСТАЯ СТРОКА
print('ПРОСТАЯ СТРОКА'.lower())  # простая строка
print('рарара'.count('ра'))  # 3
print('рарара'.count('ра', 2, 4))  # 1
print('рарара'.replace('ра', 'не'))  # 'ненене'
print('рарарара'.index('ра'))  # 0
print('рарарара'.index('ра', 4, 6))  # 4
print('рарарара'.find('ра', 4, 6))  # 4
print('рарарара'.find('ра', 10, 20))  # -1

# Взятие элемента по индексу

s = 'text.file.zip'
b = s.split('.')  # ['text', 'file', 'zip']
b[-1]  # 'zip'

if s[:-3] == 'file.':
    print('!zip')

s = '0123456789'
print(s[4:7])  # 456
print(s[7:10])  # 789
print(s[3:-3])  # 3456
print(s[:5])  # 01234
print(s[3:])  # 3456789
print(s[:])  # 0123456789
print(s[::-1])  # 9876543210
print(s[1:7:2])  # 135

# Тип данных: список

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = list('0123456789')
# s = [int(x) for x in s]
print(s[4:7])  # 456
print(s[7:10])  # 789
print(s[3:-3])  # 3456
print(s[:5])  # 01234
print(s[3:])  # 3456789
print(s[:])  # 0123456789
print(s[::-1])  # 9876543210
print(s[1:7:2])  # 135

s.sort(reverse=True)




w = [0,1,2,3,4,5,6,7,8,9]
w = [x for x in range(10)]
w = [x for x in range(100)]
w = [x for x in range(0, 100)]
w1 = [x for x in w if x >= 10]

v = []
for i in range(0, 10):
    v.extend([i, i + 2])

v = []
for i in range(0, 10):
    v.append([i, str(i)])

# Тип данных: множество

v0 = [x for x in range(5)]
v1 = [x for x in range(3, 8)]
list(set(v0) & set(v1))
list(set(v0) | set(v1))
list(set(v0) ^ set(v1))
list(set(v0) - set(v1))

# Тип данных: словарь
# Словарь — неупорядоченный набор произвольных объектов с доступом по ключу.
# Один из вариантов создания словаря — с помощью функции dict().

dct0 = {'key1': 'value1', 'key2': '1'}

dct1 = {0: '0', 1: '1'}

keys = ['k_' + str(x) for x in range(5)]
values = [x / 3.3 for x in range(0, 15, 3)]
dct2 = dict(zip(keys, values))

# Цикл задаёт многократное выполнение оператора.
# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла.
# Оператор break досрочно прерывает цикл.
# Пример сохранить в новый список все числа из первого списка, которые нацело делятся на 3:

v = [x for x in range(100)]
w = []

for i in range(len(v)):
    x = v[i]
    if x >= 50:
        # инструкция break при выполнении немедленно заканчивает выполнения цикла
        break
    if i % 3 == 0:
        # переходим к проверке условия цикла,
        # пропуская все операторы за инструкцией
        w.append(i)
        continue
        print('add')

n = int(input("Enter number: "))
i = n + n * n + n * n * n
print(i)

sec = 3651
chas = sec // 3600
ost_sec = sec - chas * 3600

minutes = ost_sec // 60
sec1 = ost_sec - minutes * 60

print("Время :", chas, ":", minutes, ":", sec1)





