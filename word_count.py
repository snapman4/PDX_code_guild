import string

with open('HeartofDarkness.txt', 'r', encoding = "utf8")  as book: # file is just a variable  #since its in the same file folder - r equals just open
    text = book.read() #file is the variable not a command

text = text.lower()

#print(text)

lesser_text = text.split(text[211051:])
#print(lesser_text)

no_begin = str(lesser_text)
no_begin = no_begin.split(no_begin[:694])
heart = str(no_begin)
print(no_begin)
print(heart.find('of'))
print(heart.find('with'))
