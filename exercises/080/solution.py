import operator
let = "abcdefghijklmnopqrstuvwxyz"
liste = []
for i in range(0, 26 * 26):
    if liste.count(let[int((i / 26))] + let[operator.mod(i, 26)]) == 0:
        if liste.count(let[operator.mod(i, 26)] + let[int((i / 26))]) == 0:
            if let[int((i / 26))] != let[operator.mod(i, 26)]:
                liste.append(let[int((i / 26))] + let[operator.mod(i, 26)])
                print(let[int((i / 26))] + let[operator.mod(i, 26)])
