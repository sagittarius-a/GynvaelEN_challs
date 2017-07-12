#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def xor(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs.decode("hex"), ys.decode("hex"))).encode("hex")

with open("picture.image", "rb") as f:
    image = f.readlines()

data = ''.join(x for x in image)

i = 0
f = open("extracted.out", "wb")
# for byte in xrange(0, len(data), 8):
for byte in xrange(0, len(data), 2):
    # e1 = data[byte:byte+4].encode("hex")
    # e2 = data[byte+4:byte+8].encode("hex")
    e1 = int(data[byte].encode("hex"), 16)
    e2 = int(data[byte+1].encode("hex"), 16)

    print "--------------" 
    result = str(e2) * e1
    f.write(result)
    print "--------------" 

f.close()
