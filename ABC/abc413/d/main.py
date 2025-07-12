import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted(map(int, input().split()), key=abs)
        
        if n == 1 or n == 2:
            print("Yes")
            continue
        
        cnt_a = Counter(a)
        if len(cnt_a) == 1:
            print("Yes")
            continue
        elif len(cnt_a) == 2:
            a0, a1 = cnt_a.keys()
            if a0 == a1*-1 and abs(cnt_a[a0]-cnt_a[a1]) <= 1:
                print("Yes")
                continue
            print("No")
            continue
        
        def check(lst):
            for i in range(2, n):
                if lst[i]*lst[0] != lst[1]*lst[i-1]:
                    return False
            return True
        
        if check(a):
            print("Yes")
            continue
        
        
        print("No")
        
        
        


if __name__ == '__main__':
    main()
