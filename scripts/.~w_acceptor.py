import sys
import math

from util import EPS, format_arc


def make_W_fst(word,i):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word
    """
    
    print(format_arc(0, 0, word, word, -math.log10(i)))


if __name__ == "__main__":

    with open("../vocab/words.vocab.txt","r") as file:
    # Read the contents of the file into a list of lines
    lines = file.readlines()

# Iterate over the lines and extract the two values from each line
    for line in lines:
    # Split the line into a list of substrings based on the tab character
       substrings = line.split('\t')
    # Extract the two values from the list (assuming they are the first two elements)
       word = substrings[0]
       i = substrings[1]
       make_W_fst(word,i)
