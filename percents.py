

def percents(x, y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents(x, y):
    """Print what percentage of x is y"""
    print(str(y) + " is " + str(percents(x, y)) + " percents of " + str(x))


percents(200, 50)
print_percents(50, 20)


__author__ = 'GiSDeCain'
