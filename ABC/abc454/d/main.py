import sys


def input():
    return sys.stdin.readline().rstrip()


def main():

    for _ in range(int(input())):
        a = input()
        b = input()

        aa = []
        for A in a:
            aa.append(A)
            if len(aa) >= 4:
                if aa[-1] == ")" and aa[-2] == aa[-3] == "x" and aa[-4] == "(":
                    for _ in range(4):
                        aa.pop()
                    aa.append("x")
                    aa.append("x")
        bb = []
        for B in b:
            bb.append(B)
            if len(bb) >= 4:
                if bb[-1] == ")" and bb[-2] == bb[-3] == "x" and bb[-4] == "(":
                    for _ in range(4):
                        bb.pop()
                    bb.append("x")
                    bb.append("x")

        print("Yes" if aa == bb else "No")


if __name__ == "__main__":
    main()
