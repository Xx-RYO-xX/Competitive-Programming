def main():
    import sys

    input = sys.stdin.readline
    n = int(input()) 
    a = list(map(int, input().split()))

    from collections import Counter

    a = Counter(a)
    
    ans = 0
    for A in a:
        a[A] %=2
        if a[A] == 1:
            ans += A
 
    print(ans)

if __name__ == "__main__":
    main()
