with open("pkg/calculator.py", "r") as f:
    for i, line in enumerate(f, 1):
        print(i, repr(line))
