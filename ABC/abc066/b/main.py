import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    n = len(s)
    
    for i in range(1, n):
        S = s[:n-i]
        if len(S) % 2 == 0:
            if S[:len(S)//2] == S[len(S)//2:]:
                print(len(S))
                exit()


if __name__ == '__main__':
    sys.exit(main())
