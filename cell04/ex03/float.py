num = float(input("Give me a number: "))
round_num = round(num)

if num - round_num == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
    