def find_min_max_rows(matrix):
  """
  Args:
    matrix: Прямоугольная матрица целых чисел.
  Returns:
    Кортеж (строка с наибольшей суммой, строка с наименьшей суммой,
             сумма элементов наибольшей строки, сумма элементов наименьшей строки).
  """
  rows = len(matrix)
  cols = len(matrix[0])
  max_row_index = 0
  min_row_index = 0
  max_sum = sum(matrix[0])
  min_sum = sum(matrix[0])
  for i in range(1, rows):
    current_sum = sum(matrix[i])
    if current_sum > max_sum:
      max_sum = current_sum
      max_row_index = i
    if current_sum < min_sum:
      min_sum = current_sum
      min_row_index = i
  return matrix[max_row_index], matrix[min_row_index], max_sum, min_sum
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

max_row, min_row, max_sum, min_sum = find_min_max_rows(matrix)

print(f"Строка с наибольшей суммой: {max_row}, Сумма: {max_sum}")
print(f"Строка с наименьшей суммой: {min_row}, Сумма: {min_sum}")
