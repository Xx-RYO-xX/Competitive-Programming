import sys 
import math

def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        ans = []
        if a == 0:
            ans.append(-c / b)
        else:
            d = b**2 - 4*a*c
            if d > 0:
                ans.append((-b + math.sqrt(d)) / (2*a))
                ans.append((-b - math.sqrt(d)) / (2*a))
            elif d == 0:
                ans.append(-b / (2*a))
        
        print(len(ans), end=" ")
        print(*sorted(ans), sep=" ")


if __name__ == '__main__':
    main()
