A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
if A < B:
    print("Числа от A до B в порядке возрастания:")
    for number in range(A, B + 1):
        print(number)
else:
    print("Числа от A до B в порядке убывания:")
    for number in range(A, B - 1, -1):
        print(number)