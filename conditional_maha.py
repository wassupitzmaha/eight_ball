
import random

eight_ball_responses =[
    "It is certain",
    "It is decidedly so",
    "Without a doubt", 
    "Yes - definitely", 
    "You may rely on it", 
    "As I like it, yes", 
    "Most likely", 
    "Outlook good",
    "Yes", 
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now.",
    "Cannot predict now",
    "Concentrate and ask again,",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

random_number = random.randint(0, 19)

user_input = input("Ask your question...")

response = eight_ball_responses [random_number]

print(response)