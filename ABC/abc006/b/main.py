import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    MOD = 10007
    if n == 1 or n == 2:
        print(0)
        return 
    elif n == 3:
        print(1)
        return

    tribo = [0]*n

    tribo[2] = 1
    for i in range(3, n):
        tribo[i] = (tribo[i-1]+tribo[i-2]+tribo[i-3])%MOD
    print(tribo[-1])

if __name__ == '__main__':
    main()
