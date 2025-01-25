import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = list(map(int, input().split()))
    
    print("Yes" if all([s == sorted(s), all(100<= ss <= 675 for ss in s), all(ss%25 == 0 for ss in s)]) else "No")
    


if __name__ == '__main__':
    sys.exit(main())
