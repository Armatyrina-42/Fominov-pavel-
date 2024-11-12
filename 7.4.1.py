def gcd(a, b):
 """
 Args:
  a: Первое натуральное число.
  b: Второе натуральное число.
 Returns:
  НОД чисел a и b.
 """
 while b:
  a, b = b, a % b
 return a
def divide_fractions(a, b, c, d):
 """ 
 Args:
  a: Числитель первой дроби.
  b: Знаменатель первой дроби.
  c: Числитель второй дроби.
  d: Знаменатель второй дроби.
 Returns:
 """
 numerator = a * d
 denominator = b * c
 common_divisor = gcd(numerator, denominator)
 return numerator // common_divisor, denominator // common_divisor
# Ввод данных от пользователя
a = int(input("Введите числитель первой дроби (A): "))
b = int(input("Введите знаменатель первой дроби (B): "))
c = int(input("Введите числитель второй дроби (C): "))
d = int(input("Введите знаменатель второй дроби (D): "))
result_numerator, result_denominator = divide_fractions(a, b, c, d)
print(f"Результат деления {a}/{b} на {c}/{d}: {result_numerator}/{result_denominator}")