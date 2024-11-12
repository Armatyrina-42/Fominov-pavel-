n = int(input("Введите натуральное число n (n ≤ 9): "))
if 1 <= n <= 9:
    for i in range(1, n + 1):
        print(''.join(str(j) for j in range(1, i + 1)))
else:
    print("Некорректный ввод. Число n должно быть от 1 до 9.")
