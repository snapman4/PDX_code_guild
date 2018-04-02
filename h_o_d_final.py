import string
import operator
import re

with open('heartofdarkness.txt', 'r', encoding = "utf8") as f:
    text = f.read().lower()

filtered = ''

for i in text:
    if i in string.ascii_letters + ' ':
        filtered += i
    else:
        filtered += ' '

words = filtered.split()

list_words = {}

for i in words:
    if i in list_words:
        list_words[i] += 1
    else:
        list_words[i] = 1


sorted_list = sorted(list(list_words.items()), key=operator.itemgetter(1), reverse=True)
print("The top 10 words included are:")
print(sorted_list[:10])
