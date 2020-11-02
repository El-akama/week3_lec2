# age = int(input("enter your age: "))

# if age > 18:
#     print("give me 200 som.")
# elif age > 7:
#     print("ohh you are schoolar, give me 150 som.")
# else:
#     print("small kid - free way.")
# print("OK")


# s = input("say something: ")                
# res = "hi, cat" if s == "myau" or s == "mur" else "who are you?"                  # тернарный оператор
# print(res)

# a = 11 == 11 and 2 == 1
# b = "compare" == "compare"
# c = 11 == 11 or 22 != 100
# d = True and True
# e = False and True
# f = True and 3 == 3
# g = False and 42 != 42
# h = True or 13 == 13
# i = "swimming" == "testing"
# j = "tester" != "testing"
# k = "test" == 123
# l = 12 != 0 and 22 == 1
# m = not (True and False) 
# n = not (1 == 1 and 0 != 1)
# o = not (105 == 4 or 101 == 101)
# p = not (11 != 101 or 7 == 4)
# q = not ("testing" == "testing" and "Ted" == "Fool Guy")
# r = 8 == 4 and not ("wrestling" == 1 or 4 == 0)
# s = "spam" == "bacon" and not (3 == 4 or 7 == 7)
# t = 6 == 6 and not ("tdd" == "tdd" or "Python" == "Super")
# print(n, o, p, q, r, s, t)


# ЦИКЛЫ

# while условие :
#     тело цикла

# s = 5
# while s <= 10:                    # главное условие, а не то все, комп крашнется
#     print(s)
#     s += 1

# print("ok")


# names = ['el', 'zero', 'star']
# while len(names) > 0:
#     print(names.pop().title())

# ---------------------------------------------
# прикольно круто надо юзать
# while True:
#     name = input("enter name: ")
#     print(f"hi, {name}.")
#     q = input("to quit enter 'q': ")
#     if q.lower() == 'q':
#         break

# тоже самое ток по другому
# flag = True
# while flag:
#     name = input("enter name: ")
#     print(f"hi, {name}.")
#     flag = input("to quit enter 'Enter': ")
# --------------------------------------------------


# for переменная in объект:
#     тело цикла

# names = ['el', 'zero', 'star']

# for x in names:
#     print(x.title())


# some_str = "python"
# count = 1
# for i in  some_str:
#     print(f"this {count} iteration")
#     print(i)
#     count += 1


# nums = [1, 2, -3, 0, 5, -4]

# for  num in nums:
#     if num > 0:
#         print(f"{num} - positive")
#     elif num < 0:
#         print(f"{num} - negative")
#     else:
#         continue
#     print(num)

# ------------------------
# continue завершает итерацию и идет дальше
# break тупо завершает цикл
# --------------------------

# nums = [1, 2, -3, 0, 5, -4]
# new_list = []
# for item in nums:
#     if item > 0:
#         new_list.append(item)
#     else:
#         continue
#     print(item)
# print(new_list)

# ---------------------------------

# range(start, end, step)

# list_ = list(range(1, 11, 2))
# print(list_)


# for x in range(1, 11):
#     print(x)

# somestr = ['b', 'o', 'n', 'o', 'n', 'o']
# for x in range(len(somestr)):                   # [0,1,2,3,4,5]
#     if somestr[x] == 'o':
#         somestr[x] = 'a'
# print(''.join(somestr))                         # конвертация из листа в строку (круто) с помощью метода join


# name = "Elaman"
# print(len(name))

# print(list(range(len(name))))
# x = 3
# new = name[x]
# print(new)


# a = {"1": "2", "3": "4"}                # перебор библиотеки
# for x,y in a.items():
#     print(x,y)
