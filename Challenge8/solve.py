#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import string

"""
What we know:

1. He just multiplied it by an unknown number.
2. It's just two bytes. But there is a plot twist. Expect the unexpected.

"""
a = 1087943696176439095600323762148055792209594928798662843208446383247024

# Number is two bytes long, so go up to 0xffff (cf 2.)
for i in range(1, 0xffff, 1):
    longhex = hex(a // i)
    # Strip the 0x, so binascii can unhex it properly
    r = longhex[2:]
    try:
        text = binascii.unhexlify(r)
        # Since reading up to 65k+ values is not handy,
        # we make sure the result is composed of ascii
        # chars. We assume that the plot twist is not
        # that big
        nb_ascii = 0
        for byte in text:
            if chr(byte) in string.printable:
                nb_ascii += 1
        # Make sure it is human readable
        # This value is kinda arbitrary
        if nb_ascii > 25:
            print(f"{i}; {text}")
    except:
        pass
