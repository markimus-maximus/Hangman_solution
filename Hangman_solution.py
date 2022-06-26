'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
from typing_extensions import Self

class Hangman:
         
    
    
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
       
        self.num_lives = num_lives

        self.word_list = word_list


            
    print('The mystery word has {len(self.word)} characters')
    print(word_guessed)
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
    

    def check_letter(self, letter) -> None:
           
        #find_index_start sets the start letter of the index to 0, this changes at the bottom of the loop because the .find function only returns the first index 
        find_index_start = 0
        matched_indices = []
        # This function determines if the letter is in the word and returns the first index in the string
        word_index_2 = word.find(letter, find_index_start)
        #if the find function returns -1 then that means the letter is not in the word

        if word_index_2 > -1:
            print('Nice! "',letter,'" is in the word!')
            #the while loop continues as long as the find_index_start is lower than the length of the word
            while find_index_start < len(word):
                #the word_index is defined based on the find function output to finding indices in the word 
                word_index = word.find(letter, find_index_start)
                 #gets the next iteration of the .find function to restart by adding one to the start of the next search by adding 1 to the last index
                find_index_start = word_index + 1
                #the loop will carry on unless the loop is broken, this can be achieved when the starting index is greater
                #than the last matching letter because the find function will return a -1, this is to know to stop the loop. 
                if word_index == -1:
                    break
                #appends each iteration of the index matched indices into a list 
                matched_indices.append(word_index) 
       
        '''
       
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

    def ask_letter():
           
        while True:
            letter_input_from_user = (input("Which letter do you choose"))
            letter_length = len(letter_input_from_user)
            letter = letter_input_from_user.lower()
            word_index_ask_letter = word.find(letter, 0)
            
            if letter_length > 1 : 
                print('Please, enter just one character')
            elif  letter in word:
                check_letter(letter)
            elif letter in word_list:
                print('"{}" was already tried'.format(letter))
            elif word_index_ask_letter == -1:
                print('Sorry, "', letter, '" is not in the word.')
                print('You have',num_lives-1,'lives left')
                num_lives - 1
       
        
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    Hangman.ask_letter(Self)
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
