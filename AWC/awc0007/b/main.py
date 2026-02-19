import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    kennkyu = []
    for _ in range(n):
        m = int(input())
        kennkyu.append(set(input().split()))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for kenn in kennkyu[i]:
                if kenn in kennkyu[j]:
                    cnt += 1
            ans += 1 if cnt >= k else 0

    print(ans)


if __name__ == "__main__":
    main()
