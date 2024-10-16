#12
s = input("Введите текст: ")
def w(s):
    return ' '.join(x for x in s.split() if x.endswith('я'))
print("Слова оканчивающиеся на 'я':", w(s))