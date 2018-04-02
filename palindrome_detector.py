def enter_word_phrase():
    user_text = input("Enter a word or phrase to check if its a palindrome\n: ")
    user_text = user_text.replace(" ", "")
    if user_text[::-1] == user_text:
        return True
    else:
        return False
print(enter_word_phrase())

# def get_input():
#     user_phrase = input("Enter a word or phrase:")
#     user_phrase = user_phrase.replace(" ", "")
# print(get_input())
#
#
# def palindrome(user_phrase):
#     if user_phrase[::1] == user_phrase:
#         return True
#     else:
#         return False
