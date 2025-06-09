import sys


def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    t = input()
    a = input()
    for i in range(n):
        if t[i] == 'o' and a[i] == 'o':
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()