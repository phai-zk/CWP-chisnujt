#!/usr/bin/env python3

import sys

BASE = 8

def shrink(text: str):
    print(text[0:8])

def enlarge(text: str):
    white_space = BASE - len(text)
    print(text + ("Z" * white_space))

if len(sys.argv) < 2:
    print("none")

for word in sys.argv[1:]:
    lenght = len(word)
    if (lenght >= BASE):
        shrink(word)
        continue
    enlarge(word)