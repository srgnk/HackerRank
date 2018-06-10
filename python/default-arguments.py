raw_input = input

def print_from_stream(n, stream = None):
    if not stream:
        stream = EvenStream()
        
    for _ in range(n):
        print(stream.get_next())