import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        m, n, p = map(int, input().split())
        if m == n == p == 0: return
        is_kansenn = {i: False for i in range(1, m+1)}
        is_kansenn[p] = True
        for _ in range(n):
            a, b = map(int, input().split())
            if is_kansenn[a]:
                is_kansenn[b] = True
            if is_kansenn[b]:
                is_kansenn[a] = True
        print(sum(is_kansenn.values()))


if __name__ == '__main__':
    main()
