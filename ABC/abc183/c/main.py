import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    n, k = map(int, input().split())
    t = []
    for _ in range(n):
        t.append(list(map(int, input().split())))
        
    ans = 0
    for perm in permutations(range(1, n)):
        time = 0
        cur = 0
        for next in perm:
            time += t[cur][next]
            cur = next
        time += t[cur][0]
        if time == k:
            ans += 1

    
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
