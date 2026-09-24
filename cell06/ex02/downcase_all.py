#!/usr/bin/env python3

import sys

def downcase_all(text: str):
    return text.lower()

output = "\n".join([downcase_all(word) for word in sys.argv[1:]])
print(output)