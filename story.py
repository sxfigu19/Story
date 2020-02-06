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

    print("")
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
    print("")


def firstnight():
    print("< A little while later, you wake up to a noise from down the hall. >")
    night = input("Do you A) Go back to sleep, or B) Find out what the noise was?")
    if night == 'A':
        print("< You try to forget about the noise and go back to sleep. > ")
    else:
        print("< You walk out of your room to find Asher in the hallway, he seems to be holding a bag. >")
        print("")
        input("You: Asher? What are you doing?")
        print("< You scared Asher causing him to almost drop his bag. >")
        name = input("Asher: Oops! Oh hey, um sorry what was your name again?")
        input("You: It's " + name + ".")
        input("Asher: Right, right, " + name + ". My bad.")
        input("Asher: I was just grabbing a snack, late night munchies.")
        print("< Asher holds up a bag of potato chips and laughs. >")
        input("You: ...Um okay. Mind if I have some?")
        input("Asher: Huh? Oh sure! Take some.")
        print("< You share a bag of chips with Asher. >")
        input("Asher: So what do you think of Asunder so far?")
        chips = input(" A) This place is weird, or B) It seems pretty cool.")
        if chips == 'A':
            print("Asher: Yea it's definitely a bit weird at first, but it's not as bad as it seems.")
        else:
            print("Asher: Really? Most people find it strange at first. But you're right it's pretty cool here.")
        print("")
        input("< You stay up late talking with Asher about Asunder. >")
        print("")
        print("")


def meetingNaomi():
    print("< After a long first night, you here a loud crash in the main room. >")
    input("< You and Asher walk out and find one of the walls with a hole in it. \n   Along with Layla and some other girl who is dressed in battle armour. >")
    input("Layla: What have I told you about letting your anger getting the best of you?")
    input("???: I can't help it Layla! \n The Nankan army isn't even playing fair at this point, and we have no way of knowing their plans.")
    input("Layla: Trust me, I know. But that doesn't mean you can come in and PUNCH MY WALL!")
    input("???: I'll pay for the damage later, \n but we've been on the same line for weeks and their army is getting stronger and stronger.")
    input("???: It won't be long until they break the guard walls.")
    input("Layla: I've heard, but please don't come running into my house like that.")
    input("Layla: Especially when I have new spirits that--")
    print("< Layla and the other girl notice you and Asher standing in the hall. >")
    print("")
    input("???: Asher? What are you doing here? You should be helping out with the army.")
    input("Asher: Oh um hey Naomi! I am actually, I came here to find out which one of the new spirts could help out.")
    input("Asher: And I think I've found them!")
    print("< Asher points at you. >")
    print("")
    input("You: Wait what? I don't even have my powers.")
    input("Asher: Sure you do, it seems like your power charm appeared while you were sleeping.")
    print("")
    print("< You look down and see a necklace glowing a bright blue and white. >")
    input("Naomi: Wow kid, you're pretty powerful.")
    input("Asher: What? No fair you've got tier V Ice powers and invisibility?! Luckyyyy.")
    input("Layla: What these two mean is yes, you are powerful. \n Tier V Ice Powers is the second highest ice powers you can have. \n And then invisibility is a pretty rare power too.")
    input("Layla: Naomi and Asher, can you take them to the training grounds since they've already gained their powers?")
    print("Naomi: Sure Layla, let's go kid.")
    name = input("Hey I have a name actually. It's ")
    input("Naomi: Yea whatever let's get going.")
    input("Asher: Don't worry " + name + ". Naomi is a little intimidating at first but she's got a nice side somewhere.")
    input("Naomi: ASHER! You do realize I can hear you right?")
    input("Asher: Ha... I didn't say anything I swear.")
    print("")


def training():
    print("< All three of you walk into town into what seems to be an obstacle course. >")
    input("Naomi: Alright kid, let's see what you got.")
    input("Asher: To activate your powers, just try and focus on the energy coming from your charm.")
    power = input("What were the colors of your charm? \n A) Bright Blue and White B) Bright Red and Orange")
    if power == "A":
        print("< You feel a cold energy charge through you. \n You then realize your hands contain a blue flame with ice pieces. >")
    else:
        print("< Nothing seems to happen. Try again. >")
        training()

def trainTwo():
    print("Hello")



askName()
intro()
firstnight()
meetingNaomi()
training()
trainTwo()