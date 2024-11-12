def process_matrix(A):
  """
  Args:
      A: Квадратная матрица.
  """
  N = len(A)
  for i in range(N):
    for j in range(N):
      if A[i][j] < 0:
        A[i][j] = 0
      elif A[i][j] > 0:
        A[i][j] = 1
  for i in range(N):
    for j in range(i + 1):
      print(A[i][j], end=" ")
    print()
A = [
    [1, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]
process_matrix(A)