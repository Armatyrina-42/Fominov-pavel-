#15
a = input("Введите текст: ")
def f(t):
    c = t.count('т')
    m = t.replace('т', 'т')
    return m, c
r, p = f(a)
print(f"Т макс подряд: {p} шт.")