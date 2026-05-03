import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    r, d, x = map(int, input().split())
    ans = [x]
    for i in range(10):
        ans.append(r * ans[-1] - d)

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
