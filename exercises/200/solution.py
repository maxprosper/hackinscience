def is_prime(a):
    if a == 2:
        print(True)
        return True
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                print(True)
                return False
            else:
                print(True)
                return True
