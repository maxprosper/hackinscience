f = open('words.txt', 'r')
a = 0
g = f.read()
d = g.replace("\n", "")
for i in range(0, len(d)):
    if d[i] == "e":
        a = a + 1
print(a)

