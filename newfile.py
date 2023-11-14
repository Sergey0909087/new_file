# for i in range(10):
    # print('Hello')

# for name peremnnoi in range(count_return):
#    block_coda

# if yslovie:
#   block_coda

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
#     print('D')
# print('E')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
# for i in range(5):
#     print('D')
# print('E')

# for i in range(10):
#     print(i + 1, '--hello')

# for _ in range(5):
#     print('Python')

# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

#range(начало, конец, шаг)

# Перебор строки с помощью цикла for

# word = input()
# for char in word:
#     print(char)

# for i in range(len(word)):
#     print(word[i])

# while условие:
# блок кода

# i = 0
# while i < 10:
#     print('Hello')
#     i += 1

# for i in range(10):
    # print('Hello')

# num = int(input())
# while num != -1:
#     print('квадрат вашего числа равен: ', num ** 2)
#     num = int(input())

# while True:
#     word = input()
#     if word == 'stop':
#         break

# i = 0
# total = 0
# while i < 10:
#     print('hi')
#     total += 1

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)


# n = int(input())
# flag = False
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         flag = True
#         break
#     n //= 10
# if flag == True:
#     print('Ваше число содержит цифру семь')
# else:
#     print('ваше число не содержит цифру семь')

# while True:
# if условие 1:
#     break
    # print('Python!')
# if условие 2:
#     break

# Оператор пропуска итерации continue
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue # переходим на следующую итерацию
#     print(i)

# for i in range(1, 101):
#     if i != 7 and i != 17 and i != 29 and i !=78:
#         print(i)
# else:
#     print('END')

# a = 1
# while a < 5:
#     print('YES')
#     a = a + 1
# else:
#     print('End')

# вложенные цифры

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(3):
#     for j in range(4):
#         if i == j:
#             continue
#         print(i, j)

# flag = False
# for i in range(3):
#     for j in range(3):
#         if j == 1 and i == 2:
#             flag = True
#             break
#         print(i, j)
#     if flag == True:
#         break

word = [1, 2, 3, 4, 5, 6, 7, 237, 8, 9, 10]
for i in word:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)