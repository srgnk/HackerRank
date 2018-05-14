# POC concept. Currently only finds the best XOR result
# in the whole array

class Node:
    def __init__(self):
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

class Trie:
    def __init__(self, size):
        self.root = Node()
        self.size = size

    def add(self, number):
        node = self.root
        for digit in number:
            if digit == '1':
                if node.right is not None:
                    node = node.right
                else:
                    node.right = Node()
                    node = node.right
                    
            if digit == '0':
                if node.left is not None:
                    node = node.left
                else:
                    node.left = Node()
                    node = node.left
                    
    def find_xor_max(self, number):
        res = ''
        untouched = ''
        number_bin = dec_to_bin(number)
        to_maximize = number_bin
        
        if len(number_bin) > self.size:
            to_maximize = number_bin[len(number_bin) - self.size:]
            untouched = number_bin[:len(number_bin) - self.size]
        elif len(number_bin) < self.size:
            to_maximize = buildup_to_len(number_bin, self.size)
        
        #print("untouched: {}".format(untouched))
        #print("to maximize: {}".format(to_maximize))
        
        node = self.root
        for digit in to_maximize:
            if digit == '1':
                if node.left is not None:
                    res += '0'
                    node = node.left
                elif node.right is not None:
                    res += '1'
                    node = node.right
            elif digit == '0':
                if node.right is not None:
                    res += '1'
                    node = node.right
                elif node.left is not None:
                    res += '0'
                    node = node.left
        
        #print("res is {}".format(res))
        return bin_to_dec(res) ^ number

    def print_trie(self):
        if self.root != None:
            self._print_trie(self.root, self.size, 0, '')

    def _print_trie(self, node, size, depth, result):
        if node != None:
            #print("size = {} depth = {} node is leaf = {}".format(size, depth, node.is_leaf()))
            #if size == depth:
            if node.is_leaf() and size == depth:
                print(result)
                return
            self._print_trie(node.left, size, depth+1, result + '0')
            self._print_trie(node.right, size, depth+1, result + '1')

def dec_to_bin(number):
    return str(bin(number).replace('0b', ''))

def bin_to_dec(number):
    return int(number, 2)

def make_arr_bin(arr):
    arr_bin = [ dec_to_bin(el) for el in arr ]
    return arr_bin

def get_max_len(arr):
    return len(dec_to_bin(max(arr)))

def buildup_to_len(number, length):
    return '0' * (length - len(number)) + number

def build_trie(arr):
    max_number_len = get_max_len(arr)
    arr_bin = make_arr_bin(arr)
    trie = Trie(max_number_len)
    #print("max len = {}".format(max_number_len))
    
    for elem in arr_bin:
        trie.add(buildup_to_len(elem, max_number_len))

    return trie
                 
if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    
    trie = build_trie(range(p, q+1))
    
    res_max = 0
    for a in range(p, q + 1):
        get_max = trie.find_xor_max(a)
        if get_max > res_max:
            res_max = get_max
        
    print(res_max)