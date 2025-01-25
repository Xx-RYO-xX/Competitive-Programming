import sys
import math


def input():return sys.stdin.readline().rstrip()
    

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    for k in range(1, m + 1):
        valid = True
        for ai in a:
            if math.gcd(ai, k) != 1:
                valid = False
                break
        if valid:
            result.append(k)
    print(len(result))
    print(*result, sep="\n")

if __name__ == '__main__':
    main()
