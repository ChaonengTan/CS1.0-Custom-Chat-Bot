# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_mood_bot_response(user_response):
    #Accepted responses
    inputAccept=["great","good","epic","happy"]
    #add some bot responses to this list
    bot_response_happy = ["Epic","Neato","Awesome","Incredible"]
    bot_response_else = ["Interesting","Huhh...","I see"]
    if user_response == "done":
        return ("Ok... I see... Goodbye...")
    if user_response != "done":
        if ifIn(user_response, inputAccept):
            #TODO: use choice to randomly return a response from the list
            return choice(bot_response_happy)
        else:
            return choice(bot_response_else)
def ifIn(inputInput, inputList):
    for value in inputList:
        if value in inputInput:
            return True
    return False



print("Welcome to Mood Bot!")
print("Please enter how you are feeling")

user_response = ""
askTimes=0
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while user_response!="done":
    if askTimes==0:
        user_response = input("How are you feeling today?: ")
        bot_response = get_mood_bot_response(user_response)
        print(bot_response)
        askTimes+=1
    elif askTimes==1:
        user_response = input("How are you feeling now?: ")
        bot_response = get_mood_bot_response(user_response)
        print(bot_response)
        askTimes+=1
    else:
        user_response = input("How about now?: ")
        bot_response = get_mood_bot_response(user_response)
        print(bot_response)