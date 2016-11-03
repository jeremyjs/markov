import copy
import random

from Corpus import Corpus
from ListDict import ListDict
from isCapitalized import isCapitalized
from itertools import islice
from randomKey import randomKey


def take(n, iterable):
    return list(islice(iterable, n))


def isEndingWord(word):
    return len(word) > 0 and word[-1] in [".", "?", "!"]


class MarkovDict:
    def __init__(self, source=None, depth=1):
        self.depth = depth
        if isinstance(source, dict):
            self.dict = ListDict(source)
        if not hasattr(self, 'dict'):
            self.dict = ListDict()
        if isinstance(source, list):
            self.add(source)

    def add(self, corpus=None):
        if corpus is None:
            return
        i = self.depth
        prev_words = corpus[:i]
        rest = corpus[i:]
        for word in rest:
            for i in range(len(prev_words)):
                prev_chunk = " ".join(prev_words[-i:])
                self.dict[prev_chunk].append(word)
            prev_words = prev_words[1:] + [word]

    def merge(self, markov_dict=None):
        if markov_dict is None:
            return
        for key, values in markov_dict:
            self.dict[key].extend(values)

    def cloned(self):
        return MarkovDict(copy.deepcopy(self.dict))

    def reversed(self):
        reversed_dict = ListDict()
        for key, values in self.dict.items():
            for value in values:
                reversed_dict[value].append(key)
        return MarkovDict(reversed_dict)

    def nextWords(self, words=None):
        if words is None:
            return randomKey(self.dict, isCapitalized).split()
        last_chunk = " ".join(words[len(words)-self.depth:])
        possible_values = self.dict[last_chunk]
        if len(possible_values) == 0:
            return randomKey(self.dict).split()
        return random.choice(possible_values).split()

    def response(self, startWord=None, reverse=False):
        words = []
        if startWord is not None and startWord in self.dict:
            words.append(startWord)
        else:
            words.extend(self.nextWords())

        while not isEndingWord(words[-1]):
            if reverse and isCapitalized(words[-1]):
                break
            words.extend(self.nextWords(words))

        if reverse:
            words = words[::-1]

        return " ".join(words)


def test():
    c1 = Corpus("Big round boulder. That is a round snake.")
    c2 = Corpus("The dog is fat. The dog eats food. My dog is yellow. Your cat is yellow.")
    c3 = Corpus("Look out! Look behind you. Are you there? Are you okay? To you, I defer.")

    m1 = MarkovDict(c1)
    m2 = MarkovDict(c2, 2)
    m3 = MarkovDict(c3)

    print ("m1:", m1.response())
    print ("m1:", m1.response())
    print ("m1:", m1.response())

    print ("m2:", m2.response())
    print ("m2:", m2.response())
    print ("m2:", m2.response())

    print ("m3:", m3.response())
    print ("m3:", m3.response())
    print ("m3:", m3.response())

import sys
if len(sys.argv) > 1 and sys.argv[1] == "--test":
    test()
