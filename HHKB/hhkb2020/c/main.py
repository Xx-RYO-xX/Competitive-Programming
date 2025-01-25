import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from sortedcontainers import SortedSet
    n = int(input())
    p = list(map(int, input().split()))
    find = SortedSet(range((2*10**5)+1))
    for i in range(n):
        find.discard(p[i])
        print(find[0])


if __name__ == '__main__':
    main()
