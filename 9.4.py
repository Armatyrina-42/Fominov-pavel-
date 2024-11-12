def is_prime(n, divisor=2):
  """
  Args:
      n: Натуральное число.
      divisor: Делитель, с которого начинается проверка (по умолчанию 2).
  Returns:
      bool: True, если число n простое, False - иначе.
  """
  if n <= 1:
    return False
  if divisor * divisor > n:
    return True
  if n % divisor == 0:
    return False
  return is_prime(n, divisor + 1)
n = int(input("Введите натуральное число n (n > 1): "))
if is_prime(n):
  print("YES")
else:
  print("NO")
