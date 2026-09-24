#!/usr/bin/env python3

for i in range(0, 13):
    result = ", ".join([str(x * i) for x in range(0, 13)])
    print(f"Table de {i}: {result}")