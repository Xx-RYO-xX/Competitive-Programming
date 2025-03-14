import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())

    ans = [['.' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        j = n-i-1
        if i <= j:
            color = '#' if i%2 == 0 else '.'
            for x in range(i, j+1):
                for y in range(i, j+1):
                    ans[x][y] = color

    for ANS in ans:
        print(''.join(ANS))


if __name__ == '__main__':
    sys.exit(main())
