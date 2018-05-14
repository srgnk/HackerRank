def capitalize(string):
    for word in string.split():
        string = string.replace(word, word.capitalize())
    return string