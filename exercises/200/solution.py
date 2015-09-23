def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return(False)
        else:
            return(True)
is_prime(2)
