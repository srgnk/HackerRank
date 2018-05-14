def mutate_string(string, position, character):
    out = list(string)
    out[position] = character
    return "".join(out)