def is_prime(a):
    z = 0
    if a == 1:
        return False
    if a == 2:
        return True
    else:
        for i in range(2, int(a ** 0.5) + 2):
            if a % i == 0:
                z = 1
        if z == 1:
            return False
        else:
            return True


l = []
for y in range(100000000, 100000010):
    if is_prime(y) is True:
        l.append(y)
w = str(l)
s = w.replace("[", "")
d = s.replace("]", "")
print(d)
