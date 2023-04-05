import os
import subprocess
import sys

from tqdm import tqdm

import json

from helpers import run_cmd

# points to slp-labs/lab1/scripts
SCRIPT_DIRECTORY = os.path.realpath(__file__)


def read_test_set(fname):
    pairs = []
    with open(fname, "r") as fd:
        lines = [ln.rstrip().split("\t") for ln in fd.readlines()]

        for ln in lines:
            pairs.append((ln[0], ln[1]))
    return pairs


def edit(incorrect, correct):
    edit = run_cmd(f"bash word_edits.sh {incorrect} {correct}").rstrip().split("\n")
    edits = []
    for i in edit:
        i = i.split("\t")
        edits.append((i[0],i[1]))
        print("\t".join(i))
    return edits


def frequency_dictionary(pairs):
    dictionary = {}
    total = 0
    for pair in pairs:
        total+=1
        edit_word = edit(pair[0], pair[1])
        for j in edit_word:
            if j not in dictionary:
                dictionary[j] = 1
            else:
                dictionary[j] += 1
    dictionary = {key: item/total for key, item in dictionary.items()}
    return dictionary

if __name__ == "__main__":
    pairs = read_test_set( "../data/wiki_copy.txt")
    frequencies = frequency_dictionary(pairs)
    f = open("../syms/dictionary.txt", "w")
    f.write(str(frequencies))
    f.close()
