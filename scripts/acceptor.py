
import sys

from util import EPS, format_arc


def make_input_fst(word,length):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word
    """
    for i, c in enumerate(word):
        if i==0:
            print(format_arc(0, length+1, c, word, weight=0))
        else:
            print(format_arc(length, length + 1, c, EPS, weight=0))
        length += 1

        if i == len(word) - 1:
            #print(format_arc(length, 0, EPS, EPS, weight=0))
            print(length)
    return (length)


if __name__ == "__main__":
    f=open("../vocab/words_only.syms","r")
    dictionary=f.readlines()
    dictionary = [s.rstrip() for s in dictionary]
    length = 0
    for word in dictionary:
        length = make_input_fst(word,length)
    print("0")

