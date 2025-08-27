import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    import bisect

    for _ in range(int(input())):
        n = int(input())
        s = list(map(int, input().split()))

        ans = [s[0]]
        end = s[-1]
        s.sort()
        # print(ans[0], s, end)
        while True:
            idx = bisect.bisect_right(s, ans[-1] * 2) - 1
            ans.append(s[idx])
            # print(ans)
            if end <= ans[-1]:
                print(len(ans))
                break
            if ans[-1] == ans[-2]:
                print(-1)
                break


if __name__ == "__main__":
    main()
