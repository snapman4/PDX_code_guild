import string
import re

with open('HeartofDarkness.txt', 'r', encoding = "utf8")  as book: # file is just a variable  #since its in the same file folder - r equals just open
    text = book.read() #file is the variable not a command

text = (text.lower())
text = [(text)]
#re.sub(r'--', r'', text)
print(text)

#words = text.count("he")
# print(words)
