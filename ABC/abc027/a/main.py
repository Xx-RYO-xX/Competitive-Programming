import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    l = list(input())
    count = defaultdict(int)
    for L in l:
        count[L] += 1
    
    for L in count:
        if count[L] == 1 or count[L] == 3:
            print(L)


if __name__ == '__main__':
    sys.exit(main())
