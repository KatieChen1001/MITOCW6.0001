# Problem Set 4A
# Name: Katie Chen
# Collaborators: N/A
# Time Spent: 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    s = []
    
    if len(sequence) == 1:
        return list(sequence)
    else:
        for element in get_permutations(sequence[0:-1]): 
            for i in range(len(element)+1):
                letter = sequence[-1]
                s.append(element[:i] + letter + element[i:])
    return s
        

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input_1 = "123"
    print("Input 1: ", example_input_1)
    print("Expected Output 1: ", ["123", "132", "312", "213", "231", "321"])
    print("Actual Output 1: ", get_permutations("123"))
    

    example_input_2 = "ab*"
    print("Input 2: ", example_input_2)
    print("Expected Output 2: ", ["ab*", "a*b", "*ab", "ba*", "b*a", "*ba"])
    print("Actual Output 2: ", get_permutations("ab*"))
    
    example_input_3 = "cd!"
    print("Input 3: ", example_input_3)
    print("Expected Output 3: ", ["cd!", "c!d", "!cd", "dc!", "d!c", "!dc"])
    print("Actual Output 3: ", get_permutations(example_input_3))
    
    
