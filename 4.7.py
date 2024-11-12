n = int(input("Введите натуральное число n: "))
sum_factorials = 0
current_factorial = 1
for i in range(1, n + 1):
    current_factorial *= i  # Находим i!
    sum_factorials += current_factorial  # Добавляем i! к сумме
print("Сумма 1! + 2! + ... +", n, "!= ", sum_factorials)