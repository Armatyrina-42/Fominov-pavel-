#13
s = input("Введите текст: ")
def i(s):
    a = s.find('(')
    b = s.find(')', a)
    if a != -1 and b != -1:
        return s[a + 1:b]
    return ""
r = i(s)
print("Полученный текст:", r)