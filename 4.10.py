n = int(input("Введите количество чисел из ряда Фибоначчи (N): "))
k = int(input("Введите порядковый номер в ряду, с которого нужно начать (K): "))
def fib_sum_from_k(n, k):
    """
    Args:
        n: Количество чисел Фибоначчи.
        k: Порядковый номер в ряду, с которого нужно начать.
    Returns:
    """
    if n <= 0 or k <= 0:
        return 0
    fib_prev = 0
    fib_curr = 1
    sum_fib = 0
    for i in range(1, n + k):
        if i >= k:
            sum_fib += fib_curr
        next_fib = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = next_fib
    return sum_fib
sum_fib = fib_sum_from_k(n, k)
print(f"Сумма {n} чисел Фибоначчи, начиная с {k}-го: {sum_fib}")