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

  def response(self, message=None, startWord=None):
    if startWord != None:
      first_half = self.reverse_dict.response(startWord, reverse=True)
      first_half = " ".join(first_half.split()[:-1]) # remove keyword
      second_half = self.forward_dict.response(startWord)
      return first_half + " " + second_half
    if message != None:
      # TODO
      pass
    return self.randomResponse()

  def randomResponse(self):
    return self.forward_dict.response()
