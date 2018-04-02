# from nltk.corpus import stopwords
# from nltk.tokenize import RegexpTokenizer

with open('HeartofDarkness.txt', 'r', encoding = "utf8")  as book: # file is just a variable  #since its in the same file folder - r equals just open
    text = book.read() #file is the variable not a command

text = text.lower()

from collections import Counter
word_count_dict = Counter(w.title() for w in text if w.lower() not in text.words(text))
word_count_dict.most_common(text)

print(text)
