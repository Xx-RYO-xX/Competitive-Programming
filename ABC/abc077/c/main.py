import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_right
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    c = sorted(map(int, input().split()))

    b_to_num = []
    for B in b:
        b_to_num.append([B, n-bisect_right(c, B)])
    # print(b_to_num)
    
    for i in range(1, n)[::-1]:
        # print(i)
        b_to_num[i-1][1] += b_to_num[i][1]
    
    
    ans = 0
    for A in a:
        try:
            ans += b_to_num[bisect_right(b, A)][1]
        except:
            continue
    print(ans)
        
if __name__ == '__main__':
    sys.exit(main())
