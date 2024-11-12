A = int(input("Введите целое число A:"))
B = int(input("Введите целое число B:"))
if A <= B:
    print("Числа от A до B включительно:")
    for number in range(A, B + 1):
        print(number)
else:
    print("Ошибка: A должно быть меньше или равно B.")
    