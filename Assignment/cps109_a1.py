#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:15:31 2023

@author: swathiesureshan
"""

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
    