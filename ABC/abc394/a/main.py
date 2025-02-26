import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    ans = ''.join([char for char in s if char == '2'])
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
