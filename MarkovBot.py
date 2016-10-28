from reverse import reverseList

class MarkovBot:
  def __init__ (self, markov_dict):
    self.forward_dict = markov_dict.cloned()
    self.reverse_dict = markov_dict.reversed()

  def trainOn(self, message=None):
    if message == None:
      return
    corpus = Corpus(message)
    self.forward_dict.add(corpus)
    self.reverse_dict.add(reverseList(corpus))

  def response(self, message=None):
    return self.forward_dict.response(message)
