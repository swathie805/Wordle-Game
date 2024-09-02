#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:15:31 2023

@author: swathiesureshan
"""

'''
This is the game wordle, where you are asked to guess a five letter word.

You have 6 tries to guess the word or else you lose that word and the word will be revealed. 
There will be three rounds, so tree different words.If the word is not five letters the game 
won’t let you proceed forward and will ask you for another input. 

If the word is five letters the game will then proceed to check if the letters you entered 
are in that word. If it is in the word and in the right position it will be printed in green. 
If it is in the word but in the wrong position, it will be in yellow. However, don’t get fooled 
if the letter is yellow earlier in the word and green later (if you entered a word with the same 
letter more than once. The program won’t check for duplicates to make the game harder). 
The program tells you whether you got it right or not. If you guessed correctly it will say congrats, 
else it will present the output and the number of tries remaining and ask you to enter a word again. 
If the word is guessed correctly in the number of tries your round score will be the number of tries remaining 
multiplied by 5. Your total score will be calculated at the end of the three rounds

At the end of the three rounds it will ask you whether you want to save your score. 
If you enter y or Y it will proceed to ask your name to save the score under that name. 
If that name was already in that game in the previous game it will ask you for another name. 
Then the game will end. 

'''

import random

# function to read words from a file called fiveletter 
def fl_words(): 
    with open("fiveletter.txt", 'r') as file:
        word_list = file.readlines()
        return random.choice(word_list).strip()
 
# function to write final score to a file called scores
def saved_score(total_score):
    print("Your score:", total_score) # print score to show user their score
    saving = input("Would you like to save your score (Y / y or any other key): ") #ask user if they want to save their score
    
    # what needs to be done to when user wants to save score
    if saving == 'Y' or saving == 'y': 
        player = input("Enter your name to save your score under that name: ") # ask user for name to know who earned score later 
        
        # check if player name is already in the file
        with open("scores.txt", "r") as file:
            content = file.read()
            if player in content:
                player = input("This name already exists in the file. Try another name: ")
                with open("scores.txt", 'w') as file:
                    file.write(f"{player} score: {total_score} \n")
                print("Your score has been saved till next game. Thank you") # let user know the score has been saved 
            else:
                with open("scores.txt", 'w') as file:
                    file.write(f"{player} score: {total_score} \n")
                print("Your score has been saved till next game. Thank you") # let user know the score has been saved 
    else:
        print("Thank you")
  
# function for one round of the game wordle 
def round():
    score = 0 # initialize score
    
    word_to_guess = fl_words()
    tries = 6 # number of attempts to guess word
        
    while tries > 0:
        output = ''  #variabke to show what the player has put correctly and incorrectly
            
        guess = input("Enter a five letter word: ").lower() # getting the guess from the user 
        
        if len(guess) == 5:
            for i in range(5):
                if guess[i] in word_to_guess and guess[i] == word_to_guess[i]: # check if letter is in the hidden word and if it is in the right position
                    output += '\x1b[32m' # makes the text green
                    output += guess[i]
                    output += '\x1b[39m' # change back to default colour 
                elif guess[i] in word_to_guess: # checks if letter in word but not right position
                    output += '\x1b[1;33m' # makes the text yellow
                    output += guess[i]
                    output += '\x1b[39m' # change back to default colour 
                else: # letter not in the word
                    output += '\x1b[39m' # makes the text the default colour 
                    output += guess[i]
            
            if guess == word_to_guess: #check if they got the whole word
                print(f"Congrats! you guessed the word: {output}\n")
                score += 5 * tries # increment the score 
                return (score)
                break
            else:
                tries -= 1 # reduce the number of attempts
                print("Your guess result:", output) # display what they got right and wrong
                print("Tries left:", tries) # remaining tries before no more guesses
        else:
            print("The game will not continue if you do not enter a five letter word.")
            
    if tries == 0:
        score -= 10 # decrease points by 
        print("Oh, better luck on your next time. Your word was:", word_to_guess)
        return (score)

# play the game three times 
def wordle(): 
    total_score = 0 # initialize total score 
    
    print("\nWelcome to Wordle!") # start the game 
    # run the game to have three rounds
    for n in range(3):
        round_score = round() # take the value the function returns
        total_score += round_score # add the round scores together
    
    saved_score(total_score)
    print("End of Game!") #let the user know the game is done 


if __name__ == "__main__":
    wordle()
    