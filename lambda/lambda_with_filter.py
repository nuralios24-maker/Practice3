numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("x % 2 != 0:", odd_numbers)

num = list(filter(lambda x: x % 2 == 0, numbers))
print("x % 2 == 0:", num)

num = list(filter(lambda x: x // 2 == 0, numbers))
print("x // 2 == 0:", num)

num = list(filter(lambda x: x // 2 != 0, numbers))
print("x // 2 != 0:", num)

num = list(filter(lambda x: x > 2, numbers))
print("x > 2:", num)

num = list(filter(lambda x: x < 2, numbers))
print("x < 2:", num)
