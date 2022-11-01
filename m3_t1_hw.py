"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: 'Hello Python'
Out: 'Python Hello'
"""
first_str = input('first_str:')

for i in range(len(first_str)):
    if first_str[i] == ' ':
        pos = i
        break
print(first_str[pos + 1 :  :], first_str[: pos])


