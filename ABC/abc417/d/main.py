import sys



def input():return sys.stdin.readline().rstrip()


def main():
    import bisect
    
    n = int(input())
    pab = []
    accmb = []
    for i in range(n):
        p, a, b = map(int, input().split())
        pab.append((p, a, b))
        if i !=0:
            accmb.append(b+accmb[-1]) 
        else:
            accmb.append(b)

    q = int(input())
    for _ in range(q):
        x = int(input())
        if x > 500:
            pos = bisect.bisect_left(accmb, x-500)
            if pos >= n:
                print(x-accmb[-1])
                continue
            ans = x-accmb[pos]
            start = pos + 1
        else:
            ans = x
            start = 0
        for i in range(start, n):
            p, a, b = pab[i]
            if ans <= p:
                ans += a
            else:
                ans = ans-b if ans >= b else 0
        print(ans)


if __name__ == '__main__':
    main()
