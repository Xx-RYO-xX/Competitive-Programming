import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    d = int(input())
    a = [None]*(d+1)
    a[1] = int(input())
    for i in range(2, d+1):
        a[i] = a[i-1] + int(input())

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if a[s] < a[t]:
            print(t)
        elif a[s] > a[t]:
            print(s)
        else:
            print("Same")


if __name__ == '__main__':
    main()
