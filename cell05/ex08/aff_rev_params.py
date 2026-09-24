#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    exit(1)

parameters = "\n".join(sys.argv[:0:-1])
print(parameters)