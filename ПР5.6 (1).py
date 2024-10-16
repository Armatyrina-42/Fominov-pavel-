#6
a = input("Введите текст: ")
def f(t):
    c = t.count('а')
    m = t.replace('а', '')
    return m, c
r, p = f(a)
print("Измененный текст:", r)
print(f"Количество удалений: {p}")