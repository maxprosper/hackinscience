def love_meet(a, b):
    list = []
    for i in a:
        if i in b:
            if i not in list:
                list.append(i)
    z = set(list)
    print(z)

def affair_meet(a, b, c):
    list = []
    for i in b:
        if i in c:
            if i not in list:
                if i not in a:
                    list.append(i)
    z = set(list)
    print(z)
    
    
alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']

affair_meet(bob, alice, silvester)
