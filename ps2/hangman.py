# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    chosen_word = random.choice(wordlist)
    
    return chosen_word

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    guessed = False

    for letter in secret_word: 
        if letter in letters_guessed: 
            guessed = True
        else: 
            guessed = False
            break 
    return guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_word = []
    
    for letter in secret_word: 
        if letter in letters_guessed:
            guessed_word.append(letter)
        else: 
            guessed_word.append("_ ")
    
    guessed_word = "".join(guessed_word)
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    available_letters = string.ascii_lowercase
    
    for letter in available_letters: 
        if letter in letters_guessed: 
            available_letters = available_letters.replace(letter, "")

    return available_letters   

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses_left = 6
    warnings = 3

    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    
    letters_guessed = []
    total_score = 0
    
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    
    while guesses_left > 0: 
        
        print("You have " + str(guesses_left) + " guesses left. ")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: " + available_letters)
        
        current_guess = input("Please guess a letter: ").lower()
        if len(current_guess) > 1:
            # warn user if they input more than one letter
            # no penalty
            # not specified in assignment requirements
            print("Please only enter one letter. ")
        if current_guess.isalpha(): 
            # check if input is in the alphabet
            if current_guess in letters_guessed: 
                print("You have already guessed this letter. ")
                if warnings > 0: 
                    warnings -= 1
                    print("You have " + str(warnings) + " warnings left. ")
                else: 
                    guesses_left -= 1
            else:
                letters_guessed.append(current_guess)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if current_guess in secret_word:
                    print("Good guess: " + guessed_word)
                else: 
                    print("Oooops! That letter is not in the word: " + guessed_word)
                
                if is_word_guessed(secret_word, letters_guessed):
                    print("Congrats! You have won!")
                    unique_letters = "".join(set(secret_word))
                    total_score = guesses_left * len(unique_letters)
                    print("Your total score is " + str(total_score))
                    break
                
                if current_guess in consonants and not current_guess in secret_word:
                    # print("You guessed a consonant that is not in the word, you loose 1 guess)
                    guesses_left -= 1
                elif current_guess in vowels and not current_guess in secret_word:
                    # print("You guessed a vowel that is not in the word, you loose 2 guesses")
                    guesses_left -= 2
        else: 
            if warnings > 0: 
                warnings -= 1 
                print("Oooops that is not a valid letter. You have " + str(warnings) + " warnings left. ")
            else:
                # print("You have no warnings left. You will loose a guess")
                guesses_left -= 1
   
    if guesses_left == 0: 
        print("You have lost the game...")
        print("The secret word is " + secret_word)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word_no_space = my_word.replace(" ", "")

    match = False
    
    if len(my_word_no_space) == len(other_word):
        for my, other in zip(my_word_no_space, other_word): 
            if my.isalpha():
                if my == other: 
                    match = True
                else:
                    match = False

                    break
            else: 
                match = True
    return match

def show_possible_matches(my_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matched_words = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word): 
            matched_words.append(word)
            
    return matched_words

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses_left = 6
    warnings = 3

    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    
    letters_guessed = []
    total_score = 0
    
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    
    while guesses_left > 0: 
        
        print("You have " + str(guesses_left) + " guesses left. ")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: " + available_letters)
        
        current_guess = input("Please guess a letter: ").lower()

        if len(current_guess) > 1:
            # warn user if they input more than one letter
            # no penalty
            # not specified in assignment requirements
            print("Please only enter one letter. ")
        if current_guess.isalpha(): 
            # check if input is in the alphabet
            if current_guess in letters_guessed: 
                print("You have already guessed this letter. ")
                if warnings > 0: 
                    warnings -= 1
                    print("You have " + str(warnings) + " warnings left. ")
                else: 
                    guesses_left -= 1
            else:
                letters_guessed.append(current_guess)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if current_guess in secret_word:
                    print("Good guess: " + guessed_word)
                else: 
                    print("Oooops! That letter is not in the word: " + guessed_word)
                
                if is_word_guessed(secret_word, letters_guessed):
                    print("Congrats! You have won!")
                    unique_letters = "".join(set(secret_word))
                    total_score = guesses_left * len(unique_letters)
                    print("Your total score is " + str(total_score))
                    break
                
                if current_guess in consonants and not current_guess in secret_word:
                    # print("You guessed a consonant that is not in the word, you loose 1 guess)
                    guesses_left -= 1
                elif current_guess in vowels and not current_guess in secret_word:
                    # print("You guessed a vowel that is not in the word, you loose 2 guesses")
                    guesses_left -= 2
        elif current_guess == "*":
            possible_matches = show_possible_matches(guessed_word, wordlist)
            print("Possible matches are: ")
            print(possible_matches)
        else: 
            if warnings > 0: 
                warnings -= 1 
                print("Oooops that is not a valid letter. You have " + str(warnings) + " warnings left. ")
            else:
                # print("You have no warnings left. You will loose a guess")
                guesses_left -= 1
                
    if guesses_left == 0: 
        print("You have lost the game...")
        print("The secret word is " + secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
