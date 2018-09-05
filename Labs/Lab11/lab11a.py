
import string

def build_word_set( input_file ):    
    word_set = set()    
    for line in input_file:
        # remove spaces at beginning and end, put each word into list
        word_lst = line.strip().split()
        # makes word lower case, gets rid of any puncuation
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]        
        for word in word_lst:            
            if word != "":
                # if word is not empty string, add it to the word set
                word_set.add( word )                
    return word_set


def compare_files( file1, file2 ):

    # Build two sets:   
    #   all of the unique words in file1
    doc1_set = build_word_set(file1)
    #   all of the unique words in file2
    doc2_set = build_word_set(file2)

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    unique_set = doc1_set | doc2_set       
   
    print("Number of unique words in the two files: ",len(unique_set))
    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    both_set = doc1_set & doc2_set
    print("Number of unique words common to both files: ",len(both_set))
    
  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

