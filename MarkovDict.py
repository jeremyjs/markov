import copy, random
from ListDict import ListDict
from randomKey import randomKey
from isCapitalized import isCapitalized

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
    if corpus == None:
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
    return MarkovDict(reversed_dict)

  def nextWord(self, words=None):
    if words == None:
      return randomKey(self.dict, isCapitalized).split()[0]
    last_chunk = " ".join(words[len(words)-self.depth:])
    return random.choice(self.dict[last_chunk])

  def response(self, startWord=None, reverse=False):
    words = []
    if startWord != None and startWord in self.dict:
      words.append(startWord)
    else:
      words.append(self.nextWord())

    while not isEndingWord(words[-1]):
      words.append(self.nextWord(words))

    if reverse:
      words = words[::-1]

    return " ".join(words)


from Corpus import Corpus
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
