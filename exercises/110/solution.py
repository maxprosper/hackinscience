import sys


def is_digit(a):
    if a in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return(True)
    else:
        return(False)


def is_numeric(b):
    for i in range(0, len(b)):
        if is_digit(b[i]) is False:
            return(False)
    return(True)


def is_operator(c):
    if c in ["+", "-", "*", "^", "%", "/"]:
        return(True)
    else:
        return(False)


if len(sys.argv) == 4:
    if is_numeric(sys.argv[1]) is True:
        if is_numeric(sys.argv[3]) is True:
            if is_operator(sys.argv[2]) is True:
                if sys.argv[2] == "+":
                    print(float(sys.argv[1]) + float(sys.argv[3]))
                if sys.argv[2] == "-":
                    print(float(sys.argv[1]) - float(sys.argv[3]))
                if sys.argv[2] == "*":
                    print(float(sys.argv[1]) * float(sys.argv[3]))
                if sys.argv[2] == "/":
                    print(float(sys.argv[1]) / float(sys.argv[3]))
                if sys.argv[2] == "^":
                    print(float(sys.argv[1]) ** float(sys.argv[3]))
                if sys.argv[2] == "%":
                    print(float(sys.argv[1]) % float(sys.argv[3]))
            else:
                print("input error")
        else:
            print("input error")
    else:
        print("input error")
else:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
