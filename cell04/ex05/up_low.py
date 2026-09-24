#!/usr/bin/env python3

word = input()
new_word = ""

for i in range(len(word)):
    if word[i].isupper():
        new_word += word[i].lower()
    else:
        new_word += word[i].upper()
print(new_word)