import sys

if len(sys.argv) < 2:
    print("none")
    exit(1)

parameters = "\n".join([f"{word}: {len(word)}" for word in sys.argv[1:]])
print(f"parameters: {len(sys.argv) - 1}\n{parameters}")