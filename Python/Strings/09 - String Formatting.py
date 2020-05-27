def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    [print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(num, width = width)) for num in range(1, number+1)]
