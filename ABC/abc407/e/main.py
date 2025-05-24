import sys 

def input(): return sys.stdin.readline().rstrip()


def main():
    import heapq
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        for __ in range(2*n):
            a.append(int(input()))
        
        heap = []
        ans = 0
        for i, num in enumerate(a):
            heapq.heappush(heap, -num)
            if (i&1) == 0:
                ans += -heapq.heappop(heap)
        
        print(ans)


if __name__ == '__main__':
    sys.exit(main())
