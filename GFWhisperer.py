
from random import choice


def GFWhisperer():
    """
        This is a program teaching guys how to talk to their GF
        The key is to listen to her and be supportive
        This program will break things down and talk to you like a homie
        
        this function asks the user questions
        based on the answer to the previous question
    """
    userComment = input("GF Whisperer >> I'm here to help you with your response to your GF so that you know how to talk to her the way she wants\n type your relationship question here>> ")

    while userComment not in ["goodbye","bye","quit","exit"]:
        response = respond(userComment)
        print("GF Whisperer >> "+response)
        userComment = input("Clueless BF>> ")
    print("I hope you learned something about how to treat your GF the way she deserves today")



def respond(comment):
    """ generate a computer response to the user's comment"""
    if contains(comment,GFAngery):
        return choice(AngResponses)

    if contains(comment,GFsad):
        return choice(sadResponses)

    if contains(comment,confirm):
        return choice(yesResponses)

    if contains(comment,deny):
        return choice(noResponses)

    if contains(comment,post):
        return choice(postResponses)

    if contains(comment, complain):
        return choice(complainRes)
    
    return choice(GEN)


def contains(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the mad keywords and responds to when your GF is mad at you
GFAngery = "mad angry upset hate anger wrath tantrum throw throwing smash smashing mean".split()
AngResponses = [
  "Ask her why she is mad at you, bro",
  "Just apologize to her man",
  "Ask her What's wrong",
  "Did you do something that she doesn't like?",
  "Did you forget about her birthday or aniversary?"  
]

# Here are some sad keywords and responds to when your GF is sad 
GFsad = "sad down blue depressed depression lonely".split()
sadResponses=[
    "Bro you gotta comfort her somehow",
    "Try to be there for her and keep her companied",
    "You need to give her more attention",
    "She needs you help man but give her comfort not solution",
    "Just be extra nice to her man"
]


# Here are when you agree with the previous respond
confirm = "yes ya yeah yee ok right correct yesh yeesh yeeesh".split()
yesResponses=[
    "I told you man!",
    "I'm glad you noticed that",
    "This is what i'm talking about",
    "ya...",
    "Then you know what to do from now on"
]
    

#Here are when you disagree with the previous respond
deny = "no not don't dont nah ney didn't didnt".split()
noResponses=[
    "What do you think the problem is then?",
    "What else is going on?",
    "If you know what's going down, go fix it",
    "You gotta make it up to ur GF",
    "Do you think it's something else?",
    "yuck"
]

# Here are when your GF asks you to post about her
post = "post insta instagram snapchat snap story picture".split()
postResponses=[
    "Honestly, bro, just post the darn picture",
    "She would appraciate you posting the pictures tho",
    "I think you should prob do what she tells you man, it's not that hard",
    "It would mean a lot to her",
    "I know you prob don't care but she prob do"
]

# Here are when your GF complains about things to you
complain = "complain talk listen complains complaining talks vent vents venting wrong".split()
complainRes=[
    "Just listen to her man",
    "She wants to be listened, give her your undevided attention",
    "Sometimes she just wants to vent so you don't have to try to fix everything",
    "The best response is honestly \"That sucks\", she just wants you to listen to her",
    "Give her your undevided attention, king",
    "Give her a hug",
    "Ask her if she wants space, and if she does, give her; if she doesn't, give her attention"
]

# We give these responses if there is nothing else to say!
GEN = [
  "What did your GF tell you",
  "Did your GF say anything",
  "Did you make her mad recently",
  "What did your GF say",
  "tell me more about it",
  "At the end of the day, show her more love",
  "Have you been giving her enough affection?",
  "You need to talk it out with her"
  
]


if __name__=="__main__":
    GFWhisperer()  # call GFWhisperer when run as a script
             # but not when imported
