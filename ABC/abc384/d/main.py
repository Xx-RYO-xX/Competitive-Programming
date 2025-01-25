import sys 
from collections import deque

def input():return sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    sum_a = sum(a)
    if sum_a == 0:
        if s == 0:
            print("Yes")
        else:
            print("No")
        exit()
    
    k = s // sum_a
    amari = s % sum_a
    
    if amari == 0:
        if k >=1:
            print("Yes")
        else:
            print("No")
        return
    
    a = a * 2
    current_sum = 0
    left = 0
    for right in range(len(a)):
        current_sum += a[right]
        while current_sum > amari and left <= right:
            current_sum -= a[left]
            left += 1
        if current_sum == amari:
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    main()
