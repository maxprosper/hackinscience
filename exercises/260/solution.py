def euclidean(a, b):
    z = 0
    for i in range(0, len(a)):
        y = (float(a[i]) - float(b[i])) ** 2
        z = z + y
    w = z ** 0.5
    return(w)


def opt_euclidean(a, b):
    import math
    z = 0
    for i in range(0, len(a)):
        y = math.pow(a[i] - b[i], 2)
        z = z + y
    w = math.sqrt(z)
    return(w)


def np_euclidean(a, b):
    import numpy
    z = 0
    for i in range(0, len(a)):
        y = numpy.power((float(a[i]) - float(b[i])), 2)
        z = z + y
    w = numpy.sqrt(z)
    return(w)
