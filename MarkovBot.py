from reverse import reverseList


class MarkovBot:
    def __init__(self, forward_dict, reverse_dict):
        self.forward_dict = forward_dict.cloned()
        self.reverse_dict = reverse_dict.cloned()

    def trainOn(self, message=None):
        if message is None:
            return
        corpus = Corpus(message)
        self.forward_dict.add(corpus)
        self.reverse_dict.add(reverseList(corpus))

    def response(self, message=None, topic=None):
        if topic is not None:
            first_half = self.reverse_dict.response(topic, reverse=True)
            first_half = first_half.split()
            first_half = first_half[:-1]  # remove keyword
            first_half = " ".join(first_half)
            second_half = self.forward_dict.response(topic)
            return first_half + " " + second_half
        if message is not None:
            # TODO
            pass
        return self.randomResponse()

    def randomResponse(self):
        return self.forward_dict.response()
