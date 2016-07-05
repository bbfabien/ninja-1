def addition(a, b):
    if isinstance(a, int) is not True or isinstance(b, int) is not True:
        return 'NaN'

    return int(a) + int(b)
