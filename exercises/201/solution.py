def is_letter(a):
    if a in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        return(True)
    else:
        return(False)


def is_alpha(b):
    for i in range(0, len(b)):
        if is_letter(b[i]) is False:
            return(False)
    return(True)

