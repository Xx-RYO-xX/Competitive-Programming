import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    s = list(input())
    ans = 0
    for i in range(n - 2):
        if "".join(s[i : i + 3]) == "ABC":
            ans += 1
    # print(ans)
    for _ in range(q):
        x, c = input().split()
        x = int(x) - 1
        before = [
            s[x : x + 3] if x < n - 2 else 0,
            s[x - 1 : x + 2] if 0 < x < n - 1 else 0,
            s[x - 2 : x + 1] if 1 < x else 0,
        ]

        for i in range(3):
            if before[i] != 0:
                after = before[i][:]
                after[i] = c

                before[i] = "".join(before[i])
                after = "".join(after)
                if before[i] == "ABC" and after != "ABC":
                    ans -= 1
                elif before[i] != "ABC" and after == "ABC":
                    ans += 1

        s[x] = c

        print(ans)


if __name__ == "__main__":
    main()
