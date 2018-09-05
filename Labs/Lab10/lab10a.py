
import string
from operator import itemgetter


def add_word( word_map, word ):
    """
    Parameters: word dictionary, and word
    Adds one to frequency of that word
    """
    # if the word is not already in the dict, add it, initialize it to 0
    if word not in word_map:
        word_map[ word ] = 0

    # add one to frequency
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    """
    Parameters: file and word dictonary
    Grabs words from file, strips them, calls add_word to add word to dict.
    """
    for line in in_file:

        # grab each word from each line, add it to list
        word_list = line.split()

        for word in word_list:

            # for each word, get rid of spaces and any punctuation
            word = word.strip().strip(string.punctuation).lower()
            if word: #if not white space
                add_word( word_map, word )
        

def display_map( word_map ):
    """
    Parameters: word dictionary
    make list of tuples of word and frequency, sort list and print
    """
    word_list = list()

    # add tuple of word and its frequency to a list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sort list of word and freq sorting off of alphabet
    alpha_list = sorted( word_list, key=itemgetter(0) )
    freq_list = sorted( alpha_list, key=itemgetter(1),reverse = True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    """
    Parameters: None
    opens file if exists, error message if not
    """
    while True:
        file_str = input("Enter file name: ")
        try:
            in_file = open(file_str, "r" )
            break
        except IOError:
            print( "\n*** unable to open file ***\n" )
            in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


