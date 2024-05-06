#3/01/24 
#HANGMAN GAME-PROJECT III 
#import necessary modules 
import random #to randomly select a word
from collections import Counter #to count occurrences of letters
#define a list of words(fruits) #string containing a list 
fruits = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon''' 
#use the split() function to split the string into a lost of words 
fruits=fruits.split(' ') #syntax to use the split() function 
#select a random word 
word = random.choice(fruits) 
#Game initialization 
#print a welcome message and hint for the user 
print("Guess the word! HINT:- Its a type of fruit ") 
#for printing the empty spaces for letters in the word 
for i in word:
    print("_", end = ' ')  #shows how many letters are present in the selected word 
print()
#initialize variables 
playing = True #The playing variable is a boolean flag used to control the main game loop. 
#It is initialized to True, indicating that the game is still in progress.
# The game loop (while (chances != 0) and flag == 0:) continues as long as playing is True. 
# The loop exits when the player either wins or loses the game. 

#a list to store the letters guessed by the user 
letterGuessed = '' 
chances = len(word) + 2 #total chances given to the user
flag = 0  #used to determine whether the game should continue or terminate.
correct = 0  
#use a while loop to iterate through the game 
while (chances!=0) and flag==0:   #flag is updated once the word is guessed correctly
    print()
    chances -=1  
    try:
        guess = str(input("Enter a letter:- ")) #use a try-except block to handle any other undesired input from the user 
    except:
        print("Enter a letter:- ")
        continue 
    #validation of the guess 
    if not guess.isalpha():
        print("Enter only a LETTER: ")
        continue 
    #below block of code checks if the input is greater than one 
    elif len(guess)>1: 
        print("Enter only a SINGLE letter: ")
        continue 
    #if the guessed letter has already been guessed before 
    elif guess in letterGuessed:
        print("Letter already guessed before")
        continue 
    #if the letter is guessed correctly 
    #update the letterGuessed variable 
    if guess in word:
        k=word.count(guess) #k stores the number of times the guessed letter occurs in the word 
        for x in range(k):
            letterGuessed+= guess #the guessed letter is added as many times as it occurs 
    #printing the word 
    for char in word:
        if char in letterGuessed and (Counter(letterGuessed)!=Counter(word)): #this condition ensures that all the letters are not guessed yet
            print(char, end = ' ')
            correct +=1 #increment the variable of correct guesses 
        #once all letters are guessed completely 
        elif Counter(letterGuessed)==Counter(word):  #condition for the game to end 
            print("The word is: ", word)  
            flag = 1 #condition for game to terminate 
            break #break out of for loop 
            break  #break out of while loop 
        else:
            print("_", end = ' ') 
#if the user has exhausted all of his chances 
if chances<0 and (Counter(letterGuessed)!=Counter(word)):
    print("\nYou Lose, Try Again! ") 
    print("The word was {}".format(word))
            
            
        

    