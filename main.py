#!/usr/bin/env python

import sys

from MarkovDict import MarkovDict
from Corpus import Corpus
from MarkovBot import MarkovBot
from importFile import importStrFromFile

corpora_root = "./corpora/"
corpora_filenames = ["Sorcerers-Stone-78500-words.txt"]
corpora_paths = [corpora_root + filename for filename in corpora_filenames]

def prompt():
  return input(">>> ")

def main():
  print ("Creating new markov dict...")
  full_markov_dict = MarkovDict()
  print ("Starting for loop to add corpora...")
  for corpus_path in corpora_paths:
    print ("Importing and initializing corpus with path:", corpus_path)
    corpus = Corpus(importStrFromFile(corpus_path))
    print ("Adding corpus with path '" + corpus_path + "' to markov dict...")
    full_markov_dict.add(corpus)
  print ("Initializing MarkovBot...")
  bot = MarkovBot(full_markov_dict)
  print ("\nWelcome to MarkovBot! Type a message. Type 'exit()' to quit.")
  message = prompt()
  while message != "exit()":
    print (bot.response(message))
    message = prompt()

main()
