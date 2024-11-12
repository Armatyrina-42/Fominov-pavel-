def find_max_and_index(arr):
 """
 Args:
  arr: Массив целых чисел.
 Returns:
  Кортеж (максимальный элемент, порядковый номер).
 """
 if not arr:
  return None, None # Пустой массив
 max_element = arr[0]
 max_index = 0
 for i in range(1, len(arr)):
  if arr[i] > max_element:
   max_element = arr[i]
   max_index = i
 return max_element, max_index
# Пример использования
numbers = [5, 2, 9, 1, 7, 3]
max_value, max_index = find_max_and_index(numbers)
print(f"Максимальный элемент: {max_value}, Порядковый номер: {max_index}")