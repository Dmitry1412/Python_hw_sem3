# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5
import math
import random
len_list1 = 5
k = 6

def CreatedList(len_list):
    list_user = list()
    for i in range(len_list):
        list_user.append(random.randint(0, 6))
    return list_user

list_1 = CreatedList(len_list1)

diff = abs(list_1[0] - k)
el_list = list_1[0]
for el in list_1:
    if abs((el - k)) < diff:
        diff = abs(el - k)
        el_list = el
        
print(list_1)
print(k)
print(el_list)
        