import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    
    ans = set()
    for i in range(n):
        for j in range(n):
            if i != j:
                ans.add(s[i]+s[j])
    
    print(len(ans))


if __name__ == '__main__':
    main()
