# Задание 1

def function1():
    try:
        a = int(input("Введите число "))
        b = int(input("Введите второе число "))
        c = a / b
        return c
    except ZeroDivisionError:
        return print("На ноль делить нельзя")


print(f"Ответ {function1()}")


# Задание 2

def function2(name, surname, age, town, email, phone):
    return print(
        f"Меня зовут {surname} {name}, мне {age} лет, мой родной город {town}, мои контактные данные {email}, {phone}")


u_name = input("Введите ваше имя ")
u_surname = input("Введите вашу фамилию ")
u_age = input("Введите ваш возраст ")
u_town = input("Введите ваш родной город ")
u_email = input("Введите вашу почту ")
u_phone = input("Ввкдите ваш номер телефона ")

function2(name=u_name, surname=u_surname, age=u_age, town=u_town, email=u_email, phone=u_phone)


# задание 2 - 2 вариант

def function2(name, surname, age, town, email, phone):
    return print(
        f"Меня зовут {surname} {name}, мне {age} лет, мой родной город {town}, мои контактные данные {email}, {phone}")


u_info = input("Введите ваше имя, фамилию, возраст, родной город, номер телефона, адрес почты через пробел")
u_info2 = u_info.split()
u_name, u_surname, u_age, u_town, u_phone, u_email = u_info2

function2(name=u_name, surname=u_surname, age=u_age, town=u_town, email=u_email, phone=u_phone)


# задание 3

def function3(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


y = int(input("Введите первое число "))
l = int(input("Введите второе число "))
p = int(input("Введите третье число "))

print(f"Сумма наибольших чисел = {function3(y, l, p)}")


# задание 3 - 2 вариант

def function3(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


numb = input("Введите три числа через пробел ")
numb2 = map(int, numb.split())
a, b, c = numb2

print(f"Сумма наибольших чисел = {function3(a, b, c)}")


# задание 4

def function4(x, y):
    return x ** y


x = int(input("Введите положительное число "))
y = int(input("Введите отрицательное число "))
print(f"{x} в степени {y} = {function4(x, y)}")


# задание 4 - 2 вариант решения

def function5(x, y):
    n = 1
    u = x
    while n < abs(y):
        u = u * x
        n += 1
    return 1 / u


x = int(input("Введите положительное число "))
y = int(input("Введите отрицательное число "))
if y < 0:
    print(f"{x} в степени {y} = {function5(x, y)}")
else:
    print("Второе число должно быть отрицательным!!!")

# задание 5

my_list1 = []
while True:
    my_str = input("Введите числа, разделенные пробелом, для остановки введите ~ ")
    if "~" in my_str.split():
        last = my_str.split()
        last.remove("~")
        last1 = map(int, last)
        print(sum(last1) + sum(my_list1))
        break
    else:
        my_list = map(int, my_str.split())
        my_list1.extend(my_list)
        print(sum(my_list1))


# Задание 6

def titleword(word):
    return word.title()


user_text = input("Введите слово из латинских букв ")
print(titleword(user_text))


# Задание 7

def titlewords(*args):
    args = str(args)
    return args.title()


user_text = input("Введите текст из латинских букв ")
print(titlewords(user_text))

