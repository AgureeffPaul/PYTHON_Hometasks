# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) 
# пользователь вводит с клавиатуры.

# ВАРИАНТ 1

# n = int(input("Введите количество монет: "))
# coins = list(map(int, input("Введите состояние каждой монеты (0 - решка, 1 - герб) через пробел: ").split()))
# heads_count = sum(coins)
# flip_count = 0
# if heads_count >= n - heads_count:
#     for i in range(n):
#         if coins[i] == 0:
#             coins[i] = 1
#             flip_count += 1
# else:
#     for i in range(n):
#         if coins[i] == 1:
#             coins[i] = 0
#             flip_count += 1

# print("Минимальное количество переворотов: ", flip_count)

# ВАРИАНТ 2

num = int(input('Введите количество монет: '))
heads = 0 # орел 1
tails = 0 # решка 0

for i in range(num):
        current_coin_status = int(input(f'Введите положение монеты {i+1} - 0 или 1:  '))
        if current_coin_status == 0: tails += 1
        if current_coin_status == 1: heads += 1

min_remove_coins = min (heads, tails)
print(f"Минимальное количество переворотов равно: {min_remove_coins}")