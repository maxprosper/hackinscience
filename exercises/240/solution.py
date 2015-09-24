a = [1, 2, 3]
for i in range(0, 7):
    b = a[-1] + a[-2]
    a.append(b)
z = str(a)
c = z.replace("[", "")
d = c.replace("]", ".")
print(d)
