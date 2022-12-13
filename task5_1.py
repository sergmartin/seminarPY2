""" Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
in
Number of words: 10

out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба"""

import random

txt = "абв"
print("Буквы из которых будет состоять слова")
print(f"Слово которое нужно удалить из текста:  {txt}")
count_word = (int(input("Количество слов в тексте: ")))
list_word = []
print("Рандомный текст: ", end=" ")
for x in range(count_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

print("Текст без абв: ", end=" ")
list_word2 = list(filter(lambda x: txt not in x, list_word))
print(" ".join(list_word2))