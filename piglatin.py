
vowel = ["a", "e", "i", "o", "u"]

def user_word():
    user_text = input("Give me a word to convert to pig latin: ").lower()
    if user_text[0] in vowel:
        user_text = user_text + "yay"
    else:
        user_text = user_text[1:] + user_text[0] + "ay"
    return user_text
print(user_word())

# user_word_converted = user_text
# print(user_word_converted)
