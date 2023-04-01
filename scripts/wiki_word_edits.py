import os
import subprocess
import sys

from tqdm import tqdm

from helpers import run_cmd

# points to slp-labs/lab1/scripts
SCRIPT_DIRECTORY = os.path.realpath(__file__)


def read_test_set(fname):
    pairs = []
    with open(fname, "r") as fd:
        lines = [ln.strip().split("\t") for ln in fd.readlines()]

        for ln in lines:
            pairs.append((ln[0], ln[1]))
    return pairs


def edit(incorrect, correct):
    edit = run_cmd(f"bash word_edits.sh {incorrect} {correct}").strip().split("\t")
    return edit


def frequency_dictionary(pairs):
    dictionary = {}
    for pair in pairs:
        edit_word = edit(pair[0], pair[1])
        edit_word_pair = (edit_word[0], edit_word[1])

        if edit_word_pair not in dictionary:
            dictionary[edit_word_pair] = 1
        else:
            dictionary[edit_word_pair] += 1

    return dictionary

if __name__ == "__main__":

    pairs = read_test_set( "../data/wiki.txt")
    frequencies = frequency_dictionary(pairs)
    for key in frequencies:
        print("{} \t {}").format(key[0], key[1])
