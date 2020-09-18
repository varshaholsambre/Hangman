
my_dict = {0:"ear", 1:"deer", 2:"snow", 3:"summer", 4:"candle", 5:"basketball", 
6:"computer", 7:"school", 8:"awkward", 9:"bagpipes", 10:"jazz"}

name = input("What is your name? ")
print ("Hello, " + name + "!" + " Are you ready to play Hangman?")
print ("Pick a number 0-10 to choose your word for Hangman!")
print ("Good luck!")

word = int(input("Enter a number 0-10: "))

if word == 0:
    print ("hint: body part")
if word == 1:
    print ("hint: animal")
if word == 2:
    print ("hint: winter")
if word == 3:
    print ("hint: season")
if word == 4:
    print ("hint: smell")
if word == 5:
    print ("hint: sport")
if word == 6:
    print ("hint: technology")
if word == 7:
    print ("hint: education")
if word == 8:
    print ("hint: personality type")
if word == 9:
    print ("hint: music instrument")
if word == 10:
    print ("hint: music type")

guesses = ("")
tries = 10
while tries > 0:
    for letter in my_dict[word]:      
        if letter in guesses:    
            print (letter),
        else:
            print ("__"),
    print ("")
    
    # lines 51 - 58 written by vishakha holsambre
    complete = True
    for char in my_dict[word]:
        if char not in guesses:
            complete = False
            break
    if complete == True:
        print("You win!! :)")
        break
    
    letter = input("Guess a letter: ")
    if letter not in my_dict[word]:  
        tries = tries - 1        
        print ("Wrong!")
        print ("You have " + str(tries) + " more guesses left!") 
    else: 
        guesses = guesses + letter
if tries == 0:           
    print ("You Lose! :(")
    print ("The word was '" + my_dict[word] + "'")
