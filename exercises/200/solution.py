def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            print("False")
            return(False)
        else:
            print("True")
            return(True)
