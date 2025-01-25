import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    
    ans = 0
    for y in range(h):
        for x in range(w):
            if x != w-1 and "" .join(s[y][x:x+2]) == "..":
                ans += 1
            if y != h-1 and "" .join(s[y][x]+s[y+1][x]) == "..":
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()
