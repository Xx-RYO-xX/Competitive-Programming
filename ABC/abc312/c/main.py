import sys 


def input():return sys.stdin.readline().rstrip()



def main():
    import bisect
    
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    ans_kouho = set()
    for i in range(max(n, m)):
        try:
            ans_kouho.add(a[i])
            ans_kouho.add(a[i]+1)
        except IndexError:
            pass
        try:
            ans_kouho.add(b[i])
            ans_kouho.add(b[i]+1)
        except IndexError:
            pass
    
    ans = float("inf")
    # print(a)
    # print(b)
    for x in ans_kouho:
        a_idx = bisect.bisect_right(a, x)
        b_idx = bisect.bisect_left(b, x)
        b_idx = m-b_idx

        
        if b_idx <= a_idx:
            ans = min(ans, x)
        # print(x)
        # print(a_idx, b_idx)
        # print(ans)
        # print()
    
    print(ans)



if __name__ == '__main__':
    sys.exit(main())
