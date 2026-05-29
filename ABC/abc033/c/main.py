import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()

    siki = [[]]
    for i in range(0, len(s), 2):
        siki[-1].append(s[i])
        if i + 1 < len(s) and s[i + 1] == "+":
            siki.append([])

    ans = 0
    for sik in siki:
        if "0" not in sik:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
