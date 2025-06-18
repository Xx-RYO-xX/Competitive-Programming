import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    first = 0
    for _ in range(q):
        query = input()
        if query[0] == "1":
            num, p, x = map(int, query.split())
            a[(p+first-1)%n] = x
        elif query[0] == "2":
            num, p = map(int, query.split())
            print(a[(p+first-1)%(n)])
        else:
            num, k = map(int, query.split())
            first = (first+k)%n


if __name__ == '__main__':
    sys.exit(main())
