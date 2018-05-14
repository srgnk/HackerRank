#!/bin/python3

import sys

def designerPdfViewer(h, word):
    return len(word) * max(list(map(lambda x: h[ord(x) - ord('a')], word)))

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
