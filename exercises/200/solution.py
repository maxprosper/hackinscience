def is_prime(a):
    if a == 2:
        return True
    else:
        for i in range(2, int(a ** 0.5) + 2):
            print(i)
            if a % i == 0:
                return False
            else:
                return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))