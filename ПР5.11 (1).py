#11
s = input("Введите текст: ")
def l(s):
    m = 0
    c = 0
    for x in s:
        if x == 'н':
            c += 1
            m = max(m, c)
        else:
            c = 0
    return m
def r(s):
    return s.replace('!', '.')
print("Длина самой длинной последовательности 'н':", l(s))
print("Измененный текст:", r(s))