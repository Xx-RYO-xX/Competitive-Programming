import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    ans = []
    idx_C = []
    for i in range(n):
        if s[i] == "(":
            idx_C.append(len(ans))
        elif s[i] == ")":
            if idx_C:
                del ans[idx_C.pop():]
                continue
        ans.append(s[i])
    
    print(*ans, sep="")

if __name__ == '__main__': 
    main()
