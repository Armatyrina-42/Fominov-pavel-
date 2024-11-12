n = int(input("Введите натуральное число n: "))
sum_of_cubes = 0
for i in range(1, n + 1):
    sum_of_cubes += i ** 3
print("Сумма 1^3 + 2^3 + ... + n^3 =", sum_of_cubes)