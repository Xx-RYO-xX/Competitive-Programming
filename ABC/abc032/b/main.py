import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    k = int(input())
    if len(s) < k:
        print(0)
        return
    ans = set()
    for i in range(len(s) - k + 1):
        ans.add(s[i:i + k])
    print(len(ans))
    


if __name__ == '__main__':
    main()
