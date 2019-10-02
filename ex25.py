# Even more practice

# uses the split function to separte the string (on the space) and makes a list
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# take the returned list, sorts it and puts in a list
def sort_words(words):
    """Sorts the Words."""
    return sorted(words)
# pops the 1st word from the list and stores in variable, then prints
def print_first_word(words):
    """prints the first word after popping it off"""
    word = words.pop(0)
    print(word)
# pops the last word in the list with the -1 param and stores it in the variable


def print_last_word(words):
    """prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)
# passed the sentence into the custom function, break_words, stores in a variable
# passes the variable into the custom function that sorts the words 
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last wors of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the wordsthen prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
