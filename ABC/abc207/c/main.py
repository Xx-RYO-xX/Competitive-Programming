import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    kukann = []
    for _ in range(n):
        t, l, r = map(int, input().split())
        kukann.append((t, l, r))
        
    def all_heikuukann(t, l, r):
        if t == 1:
            return l, r
        elif t == 2:
            return l, r-0.5
        elif t == 3:
            return l+0.5, r
        else:
            return l+0.5, r-0.5
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            l, r = all_heikuukann(*kukann[i])
            ll, rr = all_heikuukann(*kukann[j])
            if max(l,ll) <= min(r,rr):
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()
