#!/usr/bin/env python3

def famous_births(person: dict):
    person_list = sorted(list(person.values()), key=lambda x: x["date_of_birth"])
    output = "\n".join([
        f"{person["name"]} is a great scientist born in {person["date_of_birth"]}." 
        for person in person_list
    ])
    print(output)

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
