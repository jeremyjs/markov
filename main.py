#!/usr/bin/env python

import os
from pprint import pprint
import sys

from Corpus import Corpus
from importFile import importStrFromFile
from MarkovBot import MarkovBot
from MarkovDict import MarkovDict


def corporaPaths():
    corpora_root = "./corpora/"
    corpora_filenames = [
        # "Sorcerers-Stone-78500-words.txt"
        "hunger-games.txt"
        # "test/depth.txt"
    ]
    corpora_paths = [corpora_root+filename for filename in corpora_filenames]
    # exceptions = [
    #   "Sorcerers-Stone-78500-words.txt"
    # ]
    # corpora_paths = [
    #     corpora_root + filename
    #     for filename in os.listdir(corpora_root)
    #     if filename not in exceptions
    # ]
    return corpora_paths


def prompt():
    return input(">>> ")


def getDepth():
    if len(sys.argv) < 2:
        return 1
    if sys.argv[1] == "--depth":
        return int(sys.argv[2])
    if len(sys.argv) > 3 and sys.argv[2] == "--depth":
        return int(sys.argv[3])
    return 1


def main():
    print("Creating new markov dict...")
    forward_markov_dict = MarkovDict(source=None, depth=getDepth())
    reverse_markov_dict = MarkovDict(source=None, depth=getDepth())
    print("Starting for loop to add corpora...")
    for corpus_path in corporaPaths():
        corpus = Corpus(importStrFromFile(corpus_path))
        print("Adding corpus with path '" + corpus_path + "'...")
        forward_markov_dict.add(corpus)
        reverse_markov_dict.add(list(reversed(corpus)))
    print("Initializing MarkovBot...")
    bot = MarkovBot(forward_markov_dict, reverse_markov_dict)
    print("\nWelcome to MarkovBot! Type a message. Type 'exit()' to quit.")
    message = prompt()
    while message != "exit()":
        print(bot.response(topic=message.split()[0]))
        message = prompt()


def test():
    print("Creating new markov dict...")
    print(getDepth())
    corpus_path = "./corpora/test/depth.txt"
    corpus = Corpus(importStrFromFile(corpus_path))
    print(corpus)
    reverse_corpus = list(reversed(corpus))
    print(reverse_corpus)
    forward_markov_dict = MarkovDict(source=corpus, depth=getDepth())
    reverse_markov_dict = MarkovDict(source=reverse_corpus, depth=getDepth())
    pprint(forward_markov_dict.dict)
    pprint(reverse_markov_dict.dict)
    bot = MarkovBot(forward_markov_dict, reverse_markov_dict)
    # pprint(bot.forward_dict.dict)
    # pprint(bot.reverse_dict.dict)
    print(bot.response(topic="markov"))


if len(sys.argv) > 1 and sys.argv[1] == "--test":
    test()
else:
    main()
