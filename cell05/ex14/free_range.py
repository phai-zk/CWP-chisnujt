#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
    exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

print(list(range(start, end + 1)))