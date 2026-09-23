import sys

if len(sys.argv) < 2:
    print("none")
    exit(1)

parameters = "\n".join([f"{text}ism" for text in sys.argv[1:] if not text.endswith("ism")])
print(parameters)