
import sys
import re
from unidecode import unidecode
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
            print(length)
    return (length)


if __name__ == "__main__":
    f=open("../data/en_50k.txt","r")
    f2 = open("../vocab/words_subtitles.syms","w")
    dictionary=f.readlines()
    words = [] 
    i = 0
    for s in dictionary:
        if (i!=0):
            f2.write('\n')
        if (i==0):
            f2.write("<eps>" + '\t' + "0" +'\n')
            i += 1
        words_only = ''.join((z for z in s if not z.isdigit()))
        words_only = words_only.strip()
        words_only = re.sub(r'[^a-zA-Z\s]', "", unidecode(words_only)).lower()
        words_only = words_only.strip()
        words.append(words_only)
        f2.write(words_only + '\t' + str(i))
        i += 1
    length = 0
    for w in words:
        length = make_input_fst(w,length)

