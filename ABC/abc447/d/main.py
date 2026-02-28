import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    a = 0
    ab = 0
    ans = 0
    for S in s:
        if S == "A":
            a += 1
        elif S == "B":
            if a > 0:
                a -= 1
                ab += 1
        else:
            if ab > 0:
                ab -= 1
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
