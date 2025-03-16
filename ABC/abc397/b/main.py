import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    n = len(s)
    
    for i in range(n, 2*n+5):
        if i % 2 == 0:
            moji = ''.join('i' if i % 2 == 0 else 'o' for i in range(i))
            idx = 0
            for c in moji:
                if idx < n and s[idx] == c:
                    idx += 1
            if idx == n:
                print(i-n)
                return


if __name__ == '__main__':
    sys.exit(main())