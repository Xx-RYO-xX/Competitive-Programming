import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())

    while "#" in s:
        show = 0
        ans = []
        for i in range(len(s)):
            if s[i] == "#":
                ans.append(i + 1)
                show += 1
                s[i] = "."
            if show == 2:
                break
        print(*ans, sep=",")


if __name__ == "__main__":
    main()
