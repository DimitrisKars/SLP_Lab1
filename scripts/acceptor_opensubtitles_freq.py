
import sys
import re
import math
from unidecode import unidecode
from util import EPS, format_arc

def make_W_fst(word,i):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word
    """

    print(format_arc(0, 0, word, word, -math.log10(i)))


if __name__ == "__main__":
    f=open("../data/en_50k.txt","r")
    #f2 = open("../vocab/words_subtitles.syms","r")
    dictionary=f.readlines()
    pairs = [] 
    counter = 0
    for s in dictionary:
        splitted = s.strip().split(' ')
        #words_only = ''.join((z for z in s if not z.isdigit()))
        #words_only = words_only.strip()
        splitted[0] = re.sub(r'[^a-zA-Z\s]', "", unidecode(splitted[0])).lower()
        splitted[0] = splitted[0].strip()
        pairs.append(splitted)
        counter += int(splitted[1])
        #words.append(words_only)
        #f.write(words_only + '\t' + str(i))
        #i += 1
    for w in pairs:
        make_W_fst(w[0],int(w[1])/counter)
    print("0")

