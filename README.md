
# Hangman Word Tool.
## 1. import random module:
It will be used to randomly select a word from the word categories.

## 2. import selection:
I built the selection.py file in which,defines the word categories for different difficulty levels (Easy, Medium, Hard). Each category contains a list of words related to that category. Then this file is import in main code.

## 3. import pic:
I built the pic.py file in which,
defines the hangman pictures according to each difficulty level.

## 4. choose_difficulty (function):
This function displays available difficulty levels and asks from player to choose one. It ensures that the selected difficulty level is valid and returns the chosen difficulty level. And Check if the selected difficulty level exists.

## 5. choose_word (function):
This function takes a difficulty level and a category as arguments and returns a randomly chosen word from the specified category for the given difficulty level.

## 6.Choosing a Category (function):
In this function,ask from the player to chose a category related to the chosen difficulty level. And Check if the selected category exists for the chosen difficulty level.

## 7. play_game (function):
This function manages the gameplay, including difficulty selection, category selection, word selection.

Displaying the hangman according to the difficulty level.

Adjust the number of lives based on difficulty level. If player selected the easy difficulty then lives are 6, if player choose medium difficulty level lives become 4 and same as it is if player select hard level lives become 3.

It also display the list of underscore according to the randomly chosen word.and Display remaining lives.

And it also cheked the letter has already been guessed or not,or
display the all guessed letters by player. And if the gueesed letter is present in randomly chosen word then place letter on its right position.
And display the appropriate hangman picture. 

And player lose the live at each wrong guessed letters. So, when the lives become zero. picture of full hangman game appear and player lose the game.
or if the player fill all the blanks by right guessed letters then the game over and player win the game.
Its mean it checking for win or lose 
conditions.

At the end of game reveal the chosen word.And ask from player play again yes/not. if player select yes game start again else display this message("Thanks for playing Hangman!")

## 8.if __name__ == "__main__":
Main program execution:
The code inside this section runs only when someone directly uses your script, not when it's used as a reference (imported) in another script.



