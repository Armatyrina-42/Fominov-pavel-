#1
a = input("Введите русскоязычный текст: ")
def f(t):
    w = t.split()
    c = sum(1 for m in w if m.lower().startswith('е'))
    return c
r = f(a)
print(f"Количество слов, начинающихся с буквы 'е': {r}")