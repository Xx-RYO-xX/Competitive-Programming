import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(map(int, input().split()))

    ans = 0

    for S in s:
        is_correct = False
        for a in range(1, 1001):
            for b in range(1, 1001):
                if 4*a*b + 3*a + 3*b == S:
                    is_correct = True
        if is_correct:
            ans += 1

    print(n-ans)

if __name__ == '__main__':
    main()
