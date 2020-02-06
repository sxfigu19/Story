input("< New Player signing on. Press Enter to continue. > ")
print("")
from pyfiglet import Figlet

fig = Figlet(font='graffiti')
banner = fig.renderText("Asunder : Fall of Powers")

print(banner)
print("")
print("Hello player! I hope you're ready to start your adventure.")

def askName():
    answer = input("To enter Story Mode, type 'New Game. ")
    if answer == "New Game":
        print("< Entering Story Mode >")
    else:
        print("< Error: Wrong Command. Try again. >")
        askName()

def intro():
    print("")
    print("Long ago, there was a legend... that if you went down to the old well at midnight on a full moon \n     bringing your most prized possesion, you could unlock a portal to a new world")
    print("")
    print("Rumored that you could start a new life, in a new world, with magical abilities...")
    print("")
    input("Press Okay or Enter to continue. ")
    print("")

    print("You wake up to someone calling you. ")
    input("???: Hello? Oh you must be the last new villager! Welcome to Asunder. ")
    input("???: My name is Layla. I'm the guide for the new spirits.")
    name = input("Layla: What's your name young one? ")
    input("You: My name is " + name + ".")
    input("Layla: Nice to meet you " + name + ". Let's take you to meet the others!")
    print("You and Layla walk towards an old tower.")
    print("")
    input("You: What do you mean others?")
    input("Layla: There are many people, such as yourself, whose spirits have been brought here.")
    input("Layla: We were waiting for you so I can help you all find out your powers together.")
    input("Layla: You see here in Asunder, if your spirit has traveled here, then you will be granted magical abilities.")
    input("Layla: and it's my job to help you find them!")

    print("")
    print("You and Layla enter the old tower and you notice about five other people who look to be around your age.")
    print("")

    print("You sit next to a blonde boy who seems to be holding a flame in his hands.")
    print("???: Hey, I'm Asher! What's your name?")
    response = input("Do you A) Say nothing or B) Say your name?")
    if response == 'A':
        print("Asher: Ohhh I see you're just shy.")
        input("Asher: Don't worry, I'll be your other guide down here.")
        input("Asher: It may not be my job but I'll sure try.")
    else:
        print("Asher: Nice to meet you " + name + "! You seem pretty cool, I think we could be great friends.")

    input("Layla: Okay everyone, it's very important to understand that you must not take advantage of your powers.")
    print("Layla: Doing so could result in your spirit being sent to Nankan.")
    input("< The whole room fell silent. >")
    letter = input("Do you A) Ask about Nankan or B) Say nothing.")
    if letter == 'B':
        print("???: What in the heck is Nankan?")
    else:
        print("You: Umm.. what is Nankan actually?")


    input("Layla: Nankan is the home of our enemies, we have been fighting with them for centuries.")
    input("Layla: They've caused great damage and pain to our great home, Asunder.")
    input("Layla: When spirits take advantage of their powers and don't use them properly, they get sent to Nankan.")
    input("Layla: A place full of greed and envy.")
    input("Asher: So wait does that mean--")
    input("Layla: No more questions, it's getting pretty late and you all need to rest to charge your powers.")
    print("< You end up bunking with Asher and try to sleep >")


def firstnight():
    print("< A little while later, you wake up to a noise from down the hall. >")
    night = input("Do you A) Go back to sleep, or B) Find out what the noise was?")
    if night == 'A':
        print("< You try to forget about the noise and go back to sleep. > ")
    else:
        print("< You walk out of your room to find Asher in the hallway, he seems to be holding a bag. >")
        print("")
        input("You: Asher? What are you doing?")
        



askName()
intro()