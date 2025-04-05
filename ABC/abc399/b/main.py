import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    p = list(map(int, input().split()))
    
    r = 1
    
    p_idx = sorted([(score, i) for i, score in enumerate(p)], reverse=True)
    
    ans = [0] * n  
    i = 0  
    while i < n:
        same = []
        current_p = p_idx[i][0]
        while i < n and p_idx[i][0] == current_p:
            same.append(p_idx[i][1])
            i += 1
        
        for idx in same:
            ans[idx] = r
        
        r += len(same)
    
    print(*ans, sep="\n")


if __name__ == '__main__':
    sys.exit(main())
