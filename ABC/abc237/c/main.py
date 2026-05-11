import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    if s == s[::-1]:
        print("Yes")
        return
    if s[-1] == "a":
        acnt = 0
        acnt_b = 0
        for i in range(len(s)):
            if s[i] == "a":
                acnt += 1
            else:
                break

        for i in range(len(s))[::-1]:
            if s[i] == "a":
                acnt_b += 1
            else:
                break
        s = ["a"] * (acnt_b - acnt) + s
        if s == s[::-1]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
