import random


def randomKey(some_dict, matches=None):
    keys = set(some_dict.keys())
    if matches is not None:
        keys = [k for k in keys if matches(k)]
    return random.choice(list(keys))
