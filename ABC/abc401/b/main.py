import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    is_login = False
    ans = 0
    for _ in range(n):
        s = input()
        if s == "login":
            is_login = True
        elif s == "logout":
            is_login = False
        else:
            if not is_login and s == "private":
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    sys.exit(main())
