import sys
import math

from util import EPS, format_arc


def make_W_fst(word,i):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word
    """
    
    print(format_arc(0, 1, word, word, -math.log10(i)))


if __name__ == "__main__":

    with open("../vocab/words.vocab.txt","r") as file:
        # Read the contents of the file into a list of lines
        lines = [ln.rstrip().split("\t") for ln in file.readlines()]
    count = 0
    #print(lines)
    for l in lines:
        count += int(l[1])
    for l in lines:
        #print(l[1]/count)
        make_W_fst(l[0], float((int(l[1])/count)))
    print("1") 
