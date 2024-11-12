n = int(input("Введите количество чисел из ряда Фибоначчи (N): "))
def fib_sum(n):
    """
    Args:
        n: Количество чисел Фибоначчи.
    Returns:
        Сумма первых N чисел Фибоначчи.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_numbers = [0, 1]
        while len(fib_numbers) < n:
            next_fib = fib_numbers[-1] + fib_numbers[-2]
            fib_numbers.append(next_fib)
        return sum(fib_numbers)
sum_fib = fib_sum(n)
print(f"Сумма первых {n} чисел Фибоначчи: {sum_fib}")