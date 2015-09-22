import operator
a = 0
for i in range(1, 1000):
    if operator.mod((i / 3), 1) == 0:
        a = a + i
    else:
        if operator.mod((i / 5), 1) == 0:
            a = a + i
print(a)
