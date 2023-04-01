"""
USAGE:
    python mkfstinput.py MY_WORD > my_word.fst
OR:
    python mkfstinput.py MY_WORD | fstcompile | fstcompose - MY_SPELLCHECKER.fst | ...
"""

import sys

from util import EPS, format_arc


def make_input_fst(word,length):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word
    """
    accept_state =  90000
    #print(format_arc(0, length, c, c, weight=0))
    #length+=1
    for i, c in enumerate(word):
        if i==0:
            print(format_arc(1, length, c, word, weight=0))
        # TODO: You need to implement format_arc function in scripts/util
        else:
            print(format_arc(length, length + 1, c, EPS, weight=0))
        length += 1

        if i == len(word) - 1:
            print(format_arc(length, 0, EPS, EPS, weight=0))
            #print(length-1)
    #print(0)
    #print(accept_state)
    return (length)


if __name__ == "__main__":
    f=open("words_only.syms","r")
    dictionary=f.readlines()
    dictionary = [s.rstrip() for s in dictionary]
    #global length
    length = 1
    for word in dictionary:
        length = make_input_fst(word,length)
        #:length+=len(word)+1
    print("0")

