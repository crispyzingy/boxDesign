#! python3
# boxDesign - Print a box using any shape, size you want!


def boxPrint(symbol, width, height):
    # first-line
    print(symbol * width)

    # mid-section
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    # last-line
    print(symbol * width)


boxPrint("*", 15, 5)
