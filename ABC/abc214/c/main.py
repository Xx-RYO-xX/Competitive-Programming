import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    
    ans = t.copy()
    

    for _ in range(n):
        updated = False
        for i in range(n):
            j = (i - 1) % n
            possible_time = ans[j] + s[j]
            if possible_time < ans[i]:
                ans[i] = possible_time
                updated = True
        if not updated:
            break
    
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()
