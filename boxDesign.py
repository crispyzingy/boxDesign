#! python3
# boxDesign - Print a box using any shape, size you want!


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')
    # first-line
    print(symbol * width)

    # mid-section
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    # last-line
    print(symbol * width)


# enter 1 char symbol, width & height >= 2
boxPrint("*", 15, 5)
