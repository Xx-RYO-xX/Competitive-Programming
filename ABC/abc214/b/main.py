import sys


def input():return sys.stdin.readline().rstrip()


def main():
    s, t = map(int, input().split())
    
    ans = 0
    for a in range(s + 1):
        for b in range(s + 1):
            for c in range(s + 1):
                abcp = a + b + c
                abcm = a * b * c
                if abcp <= s and abcm <= t:
                    ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
