def is_prime(a):
    if a == 2:
        return True
    z = a ** 0.5
    for i in range(2, int(z) + 1):
        if a % i == 0:
            return False
        else:
            return True
