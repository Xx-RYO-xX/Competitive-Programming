import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from bisect import bisect_right
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    inf = float("inf")
    
    a_idx = []
    for i in range(n):
        a_idx.append((a[i], i+1))
    a_idx.sort()
    
    # print(a_idx)
    
    min_idx = []
    current_min = inf
    for tmp, idx in a_idx:
        current_min = min(current_min, idx)
        min_idx.append(current_min)
    # print(min_idx)

    for sushi in b:
        if sushi < a_idx[0][0]:
            print(-1)
            continue

        pos = bisect_right(a_idx, (sushi, inf)) - 1
        
        # print(pos)
        print(min_idx[pos])

if __name__ == '__main__':
    main()
