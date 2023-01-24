# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
find_text = "абв"
lst = [n for n in text.split() if find_text not in n]
print(f'Результат: {" ".join(lst)}')