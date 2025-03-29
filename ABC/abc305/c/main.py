import sys


def input():return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, input().split())
    s = []
    
    u = None
    for i in range(h):
        st = input()
        s.append(st)
        if u == None and "#" in st:
            u = i
    
    d = None
    for i in range(h)[::-1]:
        if d == None and "#" in s[i]:
            d = i
    
    l = None
    for i in range(w):
        st = [s[j][i] for j in range(h)]
        if l == None and "#" in st:
            l = i
            break
    
    r = None
    for i in range(w)[::-1]:
        st = [s[j][i] for j in range(h)]
        if r == None and "#" in st:
            r = i
            break
    
    for y in range(u, d+1):
        for x in range(l, r+1):
            if s[y][x] == ".":
                print(y+1, x+1)
                return
    
    # print(u, d, l, r)

if __name__ == '__main__':
    main()
