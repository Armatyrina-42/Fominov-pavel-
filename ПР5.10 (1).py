#10
s = input("Введите текст: ")
def f(s):
    return ' '.join(a.capitalize() for a in s.split())
r = f(s)
print("Измененный текст:", r)