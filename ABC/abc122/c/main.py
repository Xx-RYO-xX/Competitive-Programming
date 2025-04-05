import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    s = input()
    accm = [0]
    for i in range(1, n):
        if s[i-1:i+1] == "AC":
            accm.append(accm[-1]+1)
        else:
            accm.append(accm[-1])
    # print(accm)
    for _ in range(q):
        l, r = map(int, input().split())
        print(accm[r-1]-accm[l-1])


if __name__ == '__main__':
    main()
