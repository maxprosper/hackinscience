def sort_a_list(a):
    b = sorted(a, reverse=True)
    print(b)


def sort_by_mark(c):
    import operator
    d = sorted(c, key=operator.itemgetter(0), reverse=True)
    print(d)


def sort_by_name(e):
    import operator
    f = sorted(e, key=operator.itemgetter(1))
    print(f)


g = [[85, 'Susan Maddox'],
[84, 'Joseph Pedersen'],
[42, 'Lidia Robel'],
[37, 'Jeanette Wafer'],
[36, 'John Freeman'],
[27, 'Betty Askins'],
[22, 'Mark Osbourne'],
[12, 'Bonnie Torres'],
[6, 'Joshua Tran']]

sort_by_name(g)
