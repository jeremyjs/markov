def importStrFromFile(path):
    with open(path, 'r') as file:
        text = file.read().replace('\n', '')
    return text
