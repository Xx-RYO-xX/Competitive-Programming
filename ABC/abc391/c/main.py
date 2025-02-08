import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())

    su = [1] * n
    pos = list(range(n))
    ans = 0    
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            _, p, h = map(int, query)
            p, h = p-1, h-1  

            old_nest = pos[p]
            if su[old_nest] == 2:
                ans -= 1
            su[old_nest] -= 1
            
            if su[h] == 1:
                ans += 1
            su[h] += 1
            pos[p] = h
        else:
            print(ans)

if __name__ == '__main__':
    sys.exit(main())
