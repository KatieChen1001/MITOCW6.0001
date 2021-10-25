# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert type(shift) == int and shift < 26 and shift >= 0, "Enter an integer between 0 and 26 "
        
        self.shift = shift
        
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        
        shift_dict = {}
            
        for letter in lowercase_letters: 
            # get the index of the current letter
            index = lowercase_letters.index(letter)
            # get the shifted index
            shift_index = index + shift
            if shift_index > 25:
                shift_index = shift_index - 26
                
            shift_dict[letter] = lowercase_letters[shift_index]
        
        for letter in uppercase_letters: 
            # get the index of the current letter
            index = uppercase_letters.index(letter)
            # get the shifted index
            shift_index = index + shift
            if shift_index > 25:
                shift_index = shift_index - 26
                
            shift_dict[letter] = uppercase_letters[shift_index]
        
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        assert type(shift) == int and shift < 26 and shift >= 0, "Enter an integer between 0 and 26 "

        shift_dict = self.build_shift_dict(shift)
        
        l = list(self.message_text)
        s = []
        
        for element in l: 
            if element in string.ascii_lowercase or element in string.ascii_uppercase:
                s.append(shift_dict[element])
            else: 
                s.append(element)
                
                
        shifted_message_text = "".join(s)
    
        return shifted_message_text  

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        # self.message_text = text
        # self.valid_words = loadwords(WORDLIST)
        
        self.shift = shift
        self.encryption_dict = {}
        self.message_text_encrypted = ""

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        
        self.encryption_dict = Message.build_shift_dict(self, self.shift)
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        
        '''
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift 
        self.encryption_dict = build_shift_dict(self.shift)
        self.message_text_encrypted = apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        # Initiate the following: 
            # self.message_text = text
            # self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        max_valid_word = 0  
        max_list = []
        best_shift = 0
        
        for shift in range (26):
            
            num_of_valid_words = 0
            
            self.shift = shift
            self.message_text_decrypted = Message.apply_shift(self, self.shift)
            
            # split decrypted message by word into a list
            l = self.message_text_decrypted.split(" ")
            word_list = Message.get_valid_words(self)
            
            # count how many valid words are in the list
            for word in l: 
                if is_word(word_list, word): 
                    num_of_valid_words += 1
            
            # update the current max_valid_word
            if num_of_valid_words > max_valid_word: 
                max_valid_word = num_of_valid_words
                max_list = l
                best_shift = shift
            
        self.message_text_decrypted = " ".join(max_list)
        return (best_shift, self.message_text_decrypted)
    
            
            
if __name__ == '__main__':

    # Example test case (PlaintextMessage)
    plaintext_1 = PlaintextMessage('hello ', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext_1.get_message_text_encrypted())
    
    # My test case for plaintext
    plaintext_2 = PlaintextMessage('xyz ', 0)
    print('Expected Output: xyz')
    print('Actual Output:', plaintext_2.get_message_text_encrypted())
    
    plaintext_3 = PlaintextMessage('abc ', 25)
    print('Expected Output: zab')
    print('Actual Output:', plaintext_3.get_message_text_encrypted())

    # Example test case (CiphertextMessage)
    ciphertext_1 = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext_1.decrypt_message())

    # My test case for ciphertext
    ciphertext_2 = CiphertextMessage('ecv')
    print('Expected Output:', (24, 'cat'))
    print('Actual Output:', ciphertext_2.decrypt_message())
    
    ciphertext_3 = CiphertextMessage('eph')
    print('Expected Output:', (25, 'dog'))
    print('Actual Output:', ciphertext_3.decrypt_message())
    
    encrypted_story = get_story_string()
    cipherstory = CiphertextMessage(encrypted_story)
    decrypted_story = cipherstory.decrypt_message()
    print(decrypted_story)