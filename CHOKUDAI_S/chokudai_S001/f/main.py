import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    max = -float('inf')
    for num in a:
        if num > max:
            ans += 1
            max = num

    print(ans)

if __name__ == '__main__':
    main()
