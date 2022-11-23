# Hangman_solution

Second project with aiCore- developing a Hangman game :)

A game of Hangman based on a list of pre-determined (and adaptable) list. The code is generated within a class in order to retain state of parameters such as guessed letters, the completeness of the word and how many lives the player has left.

 Class attributes:
    `word: str`
        The word to be guessed picked randomly from the word_list
    `word_guessed: list`
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    `num_letters: int`
        The number of UNIQUE letters in the word that have not been guessed yet
    `num_lives: int`
        The number of lives the player has
    `list_letters: list`
        A list of the letters that have already been tried
    

There are different methods in this game; `ask_letter`, `check letter`, `play game`.

Ask letter asks for input from the user and accordingly carries out checks such as is the input a single letter, is the input a letter (as opposed to other characters), is the letter in the word. If the letter is in the word it sends the letter to the check_letter function which then iteratively checks through each position in the word and confirms if there is a match with the letter. If there is, the find function stops (only find one match in a list), so the start index of the find function needs to be started again at matched index +1.

The play_game method codes the logic of the game, how many lives are left remaining for the player and how many unique letters are left to be guessed in the word. If the former or latter reach 0 then the game is lost or won, respectively.

Throughout the game there are different messages depending on the inputted letter, and this helps to inform the player about the status of the game.

