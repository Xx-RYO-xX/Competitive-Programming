import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import math
    n = int(input())

    ans = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    for d in ans:
        print(d)


if __name__ == '__main__':
    main()
