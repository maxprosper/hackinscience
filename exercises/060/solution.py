import operator
let = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, 26 * 26):
    print(let[int((i / 26))] + let[operator.mod(i, 26)])
