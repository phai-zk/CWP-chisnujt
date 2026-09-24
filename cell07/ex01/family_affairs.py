#!/usr/bin/env python3

def find_red(name):
    return dupont_family[name] == "red"

def find_the_redheads(family: dict):
    return list(filter(find_red, family))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))