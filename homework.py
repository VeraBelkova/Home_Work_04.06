# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     3
#     -> 1

# n = int(input("Введите количество элементов в списке: "))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input("Введите элемент: ")))
# print(some_list)

# x = int(input("Введите число, кот нужно найти: "))
# count = 0
# for ind in range(0, len(some_list)):
#     if some_list[ind] == x:
#         count += 1
# print(count)



# Задача 18: Требуется найти в списке A самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# # *Пример:*
# # 5
# #     1 2 3 4 5
# #     6
# #     -> 5

# n = int(input("Введите количество элементов в списке: "))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input("Введите элемент: ")))
# print(some_list)
# x = int(input("Задайте число: "))

# some_list.sort()
# print(some_list)

# find = some_list[0]

# if x < some_list[0]: 
#    for ind in range(1, len(some_list)): 
#     if x - some_list[ind] > x - some_list[ind-1]:
#       find = some_list[ind]

# else:
#     for ind in range(1, len(some_list)):
#       if x - some_list[ind] < x - some_list[ind-1]:
#         find = some_list[ind]
# print(find)


