import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, R, C = map(int, input().split())
    s = input()

    direction = {'W': (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0)}

    kemuri = set()
    kemuri.add((0,0))
    
    r, c = 0, 0  
    ans = ""     
    for ch in s:
        ddr, ddc = direction[ch]
        r += ddr
        c += ddc

        if (r-R, c-C) in kemuri:
            ans += "1"
        else:
            ans += "0"

        if (r, c) not in kemuri:
            kemuri.add((r, c))
    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
