import re
import sys



import gensim
from gensim import corpora
import contractions
import numpy as np
import nltk


def download_corpus(corpus="gutenberg"):
    """Download Project Gutenberg corpus, consisting of 18 classic books

    Book list:
       ['austen-emma.txt',
        'austen-persuasion.txt',
        'austen-sense.txt',
        'bible-kjv.txt',
        'blake-poems.txt',
        'bryant-stories.txt',
        'burgess-busterbrown.txt',
        'carroll-alice.txt',
        'chesterton-ball.txt',
        'chesterton-brown.txt',
        'chesterton-thursday.txt',
        'edgeworth-parents.txt',
        'melville-moby_dick.txt',
        'milton-paradise.txt',
        'shakespeare-caesar.txt',
        'shakespeare-hamlet.txt',
        'shakespeare-macbeth.txt',
        'whitman-leaves.txt']
    """
    nltk.download(corpus)
    raw = nltk.corpus.__getattr__(corpus).raw()

    return raw


def identity_preprocess(s):
    return s


def clean_text(s):
    s = s.strip()  # strip leading / trailing spaces
    s = s.lower()  # convert to lowercase
    s = contractions.fix(s)  # e.g. don't -> do not, you're -> you are
    s = re.sub("\s+", " ", s)  # strip multiple whitespace
    s = re.sub(r"[^a-z\s]", " ", s)  # keep only lowercase letters and spaces

    return s


def tokenize(s):
    tokenized = [w for w in s.split(" ") if len(w) > 0]  # Ignore empty string

    return tokenized


def preprocess(s):
    return tokenize(clean_text(s))


def process_file(corpus, preprocess=identity_preprocess):
    lines = [preprocess(ln) for ln in corpus.split("\n")]
    lines = [ln for ln in lines if len(ln) > 0]  # Ignore empty lines

    return lines


if __name__ == "__main__":
    CORPUS = sys.argv[1] if len(sys.argv) > 1 else "gutenberg"
    raw_corpus = download_corpus(corpus=CORPUS)
    preprocessed = process_file(raw_corpus, preprocess=preprocess)

    dct = corpora.Dictionary(preprocessed)


map=[]

for i in range(np.size(dct)):
	map.append([dct[i],dct.cfs[i]])

print(len(map))


sorted_map = sorted(map, key=lambda x: x[0])
# Specify the file name, e.g., 'output.txt'
file_name = 'vocab.txt'

# Open the file in write mode and iterate through the 2D list
with open(file_name, 'w') as file:
    for row in sorted_map:
        # Convert each element in the row to a string and join them with a space or another delimiter
        line = ' '.join(str(element) for element in row)
        # Write the formatted line to the file and add a newline
        file.write(line + '\n')

# Create a list of lowercase English characters
lowercase_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#lowercase_chars.insert(ALT + 238,0)
# Initialize an empty list to store character-integer pairs
char_int_pairs = []

# Assign ascending integer indexes to each character
for idx, char in enumerate(lowercase_chars, start=1):
    char_int_pairs.append([char, idx])

# Specify the file name, e.g., 'output.syms'
file_name = 'chars.syms'

# Open the file in write mode and iterate through the char_int_pairs list
with open(file_name, 'w') as file:
    for pair in char_int_pairs:
        # Convert each element in the pair to a string and join them with a space or another delimiter
        line = ' '.join(str(element) for element in pair)
        # Write the formatted line to the file and add a newline
        file.write(line + '\n')
