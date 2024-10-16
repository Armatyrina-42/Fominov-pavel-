#14
s = input("Введите текст: ")
def w(s):
    return ' '.join(x for x in s.split() if x.startswith('а') or x.endswith('я'))
r = w(s)
print("Слова начинающиеся на 'а' и заканчивающиеся на 'я':", r)