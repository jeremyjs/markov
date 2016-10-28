import copy
import random
from ListDict import ListDict

def randomKey(some_dict):
  return random.choice(list(some_dict.keys()))

def isEndingWord(word):
  return len(word) > 0 and word[-1] in [".", "?", "!"]

class MarkovDict:
  def __init__(self, source=None):
    if isinstance(source, dict):
      self.dict = ListDict(source)
    if not hasattr(self, 'dict'):
      self.dict = ListDict()
    if isinstance(source, list):
      self.add(corpus)

  def add(self, corpus=None):
    if corpus == None:
      return
    prev_word = corpus[0]
    rest = corpus[1:]
    for word in rest:
      self.dict[prev_word].append(word)
      prev_word = word

  def merge(self, markov_dict=None):
    if markov_dict == None:
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
    return reversed_dict

  def nextWord(self, words=None):
    if words == None:
      key = randomKey(self.dict)
      return random.choice(self.dict[key])
    last_word = words[-1]
    return random.choice(self.dict[last_word])

  def response(self, message=None):
    words = [self.nextWord()]
    while not isEndingWord(words[-1]):
      words.append(self.nextWord(words))
    return " ".join(words)
