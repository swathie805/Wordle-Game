# Wordle-Game
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
