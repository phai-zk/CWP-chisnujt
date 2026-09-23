import sys
import re

if len(sys.argv) < 2:
    print("none")
    exit(1)

sentence = sys.argv[1]
word_count = sentence.count("z")

if word_count == 0:
    print("none")
else:
    print("z"*word_count)