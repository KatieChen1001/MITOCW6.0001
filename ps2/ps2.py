#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 13:10:14 2021

@author: Katie

"""

import string

# secret_word = 'apple'
# # letters_guessed = ['a', 'p', 'p','l','k']
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']


# PS2 1A
def is_word_guessed(secret_word, letters_guessed):
    
    """
    if all the letters in the secret word have been guessed (in the letters_guessed list)
        return True
    else 
        return False
    """
    
    for letter in secret_word:
        
        if letter in letters_guessed: 
            return True
            
        else:
            return False
            break
# print(is_word_guessed(secret_word, letters_guessed))

# PS2 1B 
def get_guessed_word(secret_word, letters_guessed):
    
    """
    fills in the letters guessed into the correct position of the secret word 
    """
    
    guessed_word = ""
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else: 
            guessed_word = guessed_word + "_ " 
    print("Your guess: " + guessed_word)        
    return guessed_word

# print(get_guessed_word(secret_word, letters_guessed))

# PS2 1C
def get_available_letters(letters_guessed):
    
    """
    remove the letters that have been submitted by the user from the alphabet
    """
    
    available_letters = string.ascii_lowercase
    
    for letter in letters_guessed: 
        if letter in available_letters:
            available_letters = available_letters.replace(letter, "")
    
    print("Available letters: " + available_letters)
    return available_letters

# print(get_available_letters(letters_guessed))

def print_dash():
    
    print("\n-----------------------\n")
    
            
def hangman():
    
    # load word list
    # pick a word from list
    secret_word = "cat"
    
    warnings = 3
    
    # inform user of how many letters there are in the secret_word
    print("There are " + str(len(secret_word)) + " letters in the secret word")
    
    
    
    
    
    # inform user how many guessed they have
    guesses_left = 6
    print("You have " + str(guesses_left) + " guesses left")
    
    # initiate a string to store user guess input
    
    letters_guessed = []
    get_available_letters(letters_guessed)
    
    joined_letters_guessed = "".join(letters_guessed)
    
    # print("\n")
    
    current_guess = input("Guess a letter: ")
    
    # check if input is in the alphabet or if input has more than one character
    if len(current_guess) > 1 or current_guess.isalpha() != True: 
        print("That was not a valid entry. \nPlease only enter one letter at a time")
        if warnings > 0: 
            warnings -= 1 
        else: 
            guesses_left -= 1
        print("You have " + str(warnings) + " left.")
        current_guess = input("Guess a letter: ")
    
    # check if input letter has already been guessed 
    if current_guess in joined_letters_guessed: 
        print("You have guessed this letter. ")
    
    if current_guess in secret_word: 
        print("Good guess!")
    else: 
        print("Ooops that letter is not in the word")   
    
    get_guessed_word(secret_word, letters_guessed)
    
    print_dash()
    
    
    
    
    # guesses_left -= 1
    # print("You have " + str(guesses_left) + " guesses left")
    
    # letters_guessed.append(current_guess.lower())
    # get_available_letters(letters_guessed)
    
    # current_guess = input("Guess a letter: ")
    
    
    
    
hangman()
    
    
    
    
    
    
    
    
    
