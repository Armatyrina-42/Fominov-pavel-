def get_odd_numbers_descending(arr):
  """
  Args:
    arr: Исходный одномерный массив целого типа.
  Returns:
  """
  odd_numbers = [num for num in arr if num % 2 != 0]
  if odd_numbers:
    odd_numbers.sort(reverse=True)
    return odd_numbers
  else:
    return None
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = get_odd_numbers_descending(numbers)
if odd_numbers:
  print("Новый массив с нечетными числами в порядке убывания:")
  print(odd_numbers)
else:
  print("В исходном массиве нет нечетных чисел.")