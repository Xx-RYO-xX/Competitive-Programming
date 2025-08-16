import sys


def input():return sys.stdin.readline().rstrip()


def main():
    q = int(input())
    h = []
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, x = map(int, query.split())
            h.append(x)
        else:
            ans = min(h)
            print(ans)
            h.pop(h.index(ans))


if __name__ == '__main__':
    main()
