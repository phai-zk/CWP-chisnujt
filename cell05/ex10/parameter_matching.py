import sys

if len(sys.argv) < 2:
    print("none")
    exit(1)

parameters = sys.argv[1]
inp = input("What was the parameter? ")
if inp == parameters:
    print("Good job!")
else:
    print("Nope, sorry...")