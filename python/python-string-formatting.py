def print_formatted(number):
    align = len(bin(number)[2:])
    for num in range(1, number + 1):
        n_dec = str(num)
        n_oct = oct(num)[2:]
        n_hex = hex(num)[2:].upper()
        n_bin = bin(num)[2:]
        print(n_dec.rjust(align), n_oct.rjust(align), n_hex.rjust(align), n_bin.rjust(align))