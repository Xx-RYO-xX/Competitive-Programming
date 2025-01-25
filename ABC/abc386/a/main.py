import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    abcd = list(map(int, input().split()))
    
    count = Counter(abcd)
    # print(count)
    tefuda = sorted(count.values(), reverse=True)
    if tefuda == [3,1] or tefuda == [2,2]:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    sys.exit(main())
