import math
import sys 


def input():return sys.stdin.readline().rstrip()


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input())
    
    if is_prime(n):
        print("Yes")
    else:
        print("No")
        


if __name__ == '__main__':
    main()
