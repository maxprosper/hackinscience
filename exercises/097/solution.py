def love_meet(a, b):
    list = []
    for i in a:
        if i in b:
            if i not in list:
                list.append(i)
    z = set(list)
    print(z)

alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']

love_meet(bob, alice)
