import math
def is_point_inside_circle(x, y, a, b, r):
  """
  Args:
    x: Координата x точки.
    y: Координата y точки.
    a: Координата x центра окружности.
    b: Координата y центра окружности.
    r: Радиус окружности.
  Returns:
  """
  distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
  return distance < r
a = float(input("Введите координату x центра окружности (a): "))
b = float(input("Введите координату y центра окружности (b): "))
r = float(input("Введите радиус окружности (R): "))
p1 = float(input("Введите координату x точки P (p1): "))
p2 = float(input("Введите координату y точки P (p2): "))
f1 = float(input("Введите координату x точки F (f1): "))
f2 = float(input("Введите координату y точки F (f2): "))
l1 = float(input("Введите координату x точки L (l1): "))
l2 = float(input("Введите координату y точки L (l2): "))
count = 0
if is_point_inside_circle(p1, p2, a, b, r):
  count += 1
if is_point_inside_circle(f1, f2, a, b, r):
  count += 1
if is_point_inside_circle(l1, l2, a, b, r):
  count += 1
print(f"Количество точек внутри окружности: {count}")
