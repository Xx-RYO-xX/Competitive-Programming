import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = set()
    for _ in range(n):
        a.add(int(input()))
    
    print(sorted(a)[-2])


if __name__ == '__main__':
    sys.exit(main())
