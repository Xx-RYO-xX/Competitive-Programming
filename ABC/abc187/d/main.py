import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ab = []
    a_sum, b_sum = 0, 0
    for _ in range(n):
        at, bt = map(int, input().split())
        ab.append((at, bt))
        a_sum += at
        b_sum += bt

    ab.sort(key=lambda x: sum(x), reverse = True)
    aoki = a_sum
    takahashi = 0
    # print(ab)
    for i in range(n):
        a, b = ab[i]
        aoki -= a
        takahashi += a + b
        if aoki < takahashi:
            print(i+1)
            return

if __name__ == '__main__':
    main()
