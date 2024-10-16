#3
a = input("Введите текст: ")
def f(t):
    c = t.count('.')
    m = t.replace('.', '')
    return m, c
r, p = f(a)
print("Измененный текст:", r)
print(f"Количество удалений: {p}")