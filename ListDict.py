from collections import defaultdict

def ListDict(some_dict=None):
  new_dict = defaultdict(list)
  if isinstance(some_dict, dict):
    for key, values in some_dict.items():
      new_dict[key].extend(values)
  return new_dict
