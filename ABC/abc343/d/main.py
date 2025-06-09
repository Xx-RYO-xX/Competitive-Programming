import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    
    from collections import defaultdict
    senshu_to_ten = defaultdict(int)
    ten_to_cnt = defaultdict(int)
    ten_to_cnt[0] = n
    for _ in range(t):
        a, b = map(int, input().split())
        before_ten = senshu_to_ten[a]
        senshu_to_ten[a] += b
        after_ten = senshu_to_ten[a]
        ten_to_cnt[before_ten] -=1
        if ten_to_cnt[before_ten] == 0:
            ten_to_cnt.pop(before_ten)

        ten_to_cnt[after_ten] += 1
        print(len(ten_to_cnt))
            



if __name__ == '__main__':
    sys.exit(main())
