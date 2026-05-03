import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input())

    for i in range(n):
        for j in range(n):
            cond1 = a[i][j] == "W" and a[j][i] != "L"
            cond2 = a[i][j] == "L" and a[j][i] != "W"
            cond3 = a[i][j] == "-" and a[j][i] != "-"
            if cond1 or cond2 or cond3:
                print("incorrect")
                return

    print("correct")


if __name__ == "__main__":
    main()
