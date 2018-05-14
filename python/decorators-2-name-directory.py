def person_lister(func):
    def inner(people):
        return [ func(p) for p in sorted(people, key = lambda x: (int(x[2])))]
    return inner

