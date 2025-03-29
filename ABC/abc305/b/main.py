import sys


def input():return sys.stdin.readline().rstrip()


def main():
    p, q = input().split()
    abcdef = {"A":0, "B":3, "C": 4, "D":8, "E":9, "F":14, "G":23}
    
    print(abs(abcdef[p]-abcdef[q]))


if __name__ == '__main__':
    main()
