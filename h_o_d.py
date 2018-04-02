import operator
import re
import string
# from collections import Counter


frequency = {}
document_text = open('test.txt', 'r', encoding = "utf8")
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,10}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])

#print(words, frequency[int(words > 10)]) trying this, doesn't work yet

# c = Counter(word.rstrip() for word in reader)
# print(c.most_common())

sorted_list = sort(list(frequency_list)), key=operator.itemgetter(1), reverse=True
# sorted_list = sorted(list(frequency_list.items()), key=operator.itemgetter(1), reverse=True)
print(sorted_list[:20])
