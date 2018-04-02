from random import choice
ball_responses = ["It is certain" , "It is decidedly so", "Without a doubt", "Yes definitely",
            "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
            "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
            "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good",
            "Very doubtful"]

question = input("Ask me a question so I can predict your future: ")
print(choice(ball_responses))

while True:
    play_again = input("Would you like to ask another question? If not answer done: ")
    if play_again.lower() == "done":
        break
    else:
        question = input("Ask me a question so I can predict your future: ")
        print(choice(ball_responses))
