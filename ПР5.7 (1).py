#7
s = input("Введите текст: ")
s1 = s[:(len(s) // 2)]
s2 = s[(len(s) // 2):]
for i in s1:
    if i == 'п':
        s1 = s1.replace('п', '*')
print("Измененный текст:", s1 + s2)