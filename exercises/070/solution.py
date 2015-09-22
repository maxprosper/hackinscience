import operator
let = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, 26 * 26):
    if let[int((i / 26))] == let[operator.mod(i, 26)]:
        a = 1
    else:
        print(let[int((i / 26))] + let[operator.mod(i, 26)])
