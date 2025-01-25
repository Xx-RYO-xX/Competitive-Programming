import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    masu = [0] * 4
    for i in range(n):
        masu[0] += 1
        for j in range(4)[::-1]:
            if masu[j] != 0:
                idou = masu[j]
                masu[j] = 0
                if j + a[i] < 4:
                    masu[j + a[i]] += idou
                else:
                    ans += idou

    print(ans)


if __name__ == '__main__':
    sys.exit(main())
