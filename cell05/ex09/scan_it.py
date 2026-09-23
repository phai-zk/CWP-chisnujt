import sys
import re

if len(sys.argv) != 3:
    print("none")
    exit(1)

word = sys.argv[1]
sentence = sys.argv[2]
word_count = len(re.findall(r'\b' + re.escape(word) + r'\b', sentence))

print(word_count)