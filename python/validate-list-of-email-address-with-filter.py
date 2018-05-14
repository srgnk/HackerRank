import re

def fun(email):
    #pattern = '[^@]+@[^@]+\.[^@]{1,3}'
    pattern = '^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)
    