def starts_with(a, b):
    for i in range(0, len(b)):
        z = 0
        if a[i] != b[i] or len(a[i]) != len(b[i]):
            z = 1
        if z == 1:
            return False
        else:
            return True
