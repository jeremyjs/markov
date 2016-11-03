#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.realpath(os.path.dirname("..")))

from Corpus import Corpus
from importFile import importStrFromFile
from MarkovBot import MarkovBot
from MarkovDict import MarkovDict


def test_reverse_markov_dict():
    full_markov_dict = MarkovDict(source=None, depth=1)
    corpus = Corpus(importStrFromFile("./test/corpora/reverse.txt"))
    full_markov_dict.add(corpus)
    bot = MarkovBot(full_markov_dict)
    print(bot.forward_dict.dict)
    print(bot.reverse_dict.dict)

test_reverse_markov_dict()
