import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = map(int, input().split())
    s = input()
    
    print("Yes" if "ab" in s or "ba" in s else "No")
    


if __name__ == '__main__':
    sys.exit(main())
