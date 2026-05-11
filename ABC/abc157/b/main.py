import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = []
    for _ in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    bingo = [[False] * 3 for _ in range(3)]
    for _ in range(n):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if a[i][j] == b:
                    bingo[i][j] = True
                    break
            else:
                continue
            break

    for i in range(3):
        if all(bingo[i]):
            print("Yes")
            return
    for j in range(3):
        if all([bingo[0][j], bingo[1][j], bingo[2][j]]):
            print("Yes")
            return
    if all([bingo[i][i] for i in range(3)]):
        print("Yes")
        return
    if all([bingo[2 - i][i] for i in range(3)]):
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
