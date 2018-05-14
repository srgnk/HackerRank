import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    lines = []
    for row in range(size):
        to_print = "-".join(alpha[row:size])
        lines.append(to_print[::-1] + to_print[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))
        