def perfect_shuffle(b):
    a = []
    for i in range(0, int((len(b) / 2))):
        a.append(b[i])
        a.append(b[i + int((len(b) / 2))])
    return(a)
