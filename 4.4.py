N = int(input("Введите количество чисел: "))
total_sum = 0
for _ in range(N):
    total_sum += int(input("Введите целое число: "))
print("Сумма введённых чисел:", total_sum)