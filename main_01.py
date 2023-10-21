# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1
import random
list_1 = list()
len_list1 = 10
k = int(input('Введите число: '))
count = 0
for i in range(len_list1):
    list_1.append(random.randint(0, 9)) 



for el in list_1:
    if k == el: count += 1
    
#print(list_1)
print(f'k = {count}')
print(k)
