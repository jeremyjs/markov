#!/usr/bin/env python

import os
import sys

from Corpus import Corpus
from importFile import importStrFromFile
from MarkovBot import MarkovBot
from MarkovDict import MarkovDict


def corporaPaths():
    corpora_root = "./corpora/"
    # corpora_filenames = [
    #     # "Sorcerers-Stone-78500-words.txt"
    #     "hunger-games.txt"
    # ]
    exceptions = [
      "Sorcerers-Stone-78500-words.txt"
    ]
    corpora_paths = [corpora_root + filename for filename in corpora_filenames]
    corpora_paths = [
        corpora_root + filename
        for filename in os.listdir(corpora_root)
        if filename not in exceptions
    ]
    return corpora_paths


def prompt():
    return input(">>> ")


def getDepth():
    if len(sys.argv) > 2 and sys.argv[1] == "--depth":
        return int(sys.argv[2])
    return 1


def main():
    print("Creating new markov dict...")
    full_markov_dict = MarkovDict(source=None, depth=getDepth())
    print("Starting for loop to add corpora...")
    for corpus_path in corporaPaths():
        # print ("Importing and initializing corpus with path:", corpus_path)
        corpus = Corpus(importStrFromFile(corpus_path))
        print("Adding corpus with path '" + corpus_path + "'...")
        full_markov_dict.add(corpus)
    print("Initializing MarkovBot...")
    bot = MarkovBot(full_markov_dict)
    print("\nWelcome to MarkovBot! Type a message. Type 'exit()' to quit.")
    message = prompt()
    while message != "exit()":
        print(bot.response(startWord=message))
        message = prompt()

main()
