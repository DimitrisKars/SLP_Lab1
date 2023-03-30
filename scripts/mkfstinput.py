"""
USAGE:
    python mkfstinput.py MY_WORD > my_word.fst

OR:
    python mkfstinput.py MY_WORD | fstcompile | fstcompose - MY_SPELLCHECKER.fst | ...
"""

import sys

from util import EPS, format_arc
#word_list=open("../vocab/words.vocab.txt","a")


def make_input_fst(word):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word

    """
    s, accept_state = 0, 10000

    for i, c in enumerate(word):
        # TODO: You need to implement format_arc function in scripts/util
        print(format_arc(s, s + 1, c, c, weight=0))
        s += 1

        if i == len(word) - 1:
            print(format_arc(s, accept_state, EPS, EPS, weight=0))

    print(accept_state)

def format_arc(src, dest, ilabel, olabel, weight):
    return "{} {} {} {} {:.3f}".format(src, dest, ilabel, olabel, weight)



#print(accept_state)


if __name__ == "__main__":
    word_list = sys.argv[1]
    make_input_fst(word_list)
