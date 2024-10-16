#4
a = input("Введите текст: ")
def f(t):
    c = t.count('а')
    m = t.replace('а', 'о')
    return m, c
r, p = f(a)
print("Измененный текст:", r)
print(f"Количество удалений: {p}")
print("Символов в строке: ", len(a))