import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    
    rate = defaultdict(int)
    for A in a:
        if 1 <= A <= 399:
            rate["hai"] += 1
        
        elif 400 <= A <= 799:
            rate["cha"] += 1
        
        elif 800 <= A <= 1199:
            rate["midori"] += 1
        
        elif 1200 <= A <= 1599:
            rate["mizu"] += 1
        
        elif 1600 <= A <= 1999:
            rate["ao"] += 1
        
        elif 2000 <= A <= 2399:
            rate["ki"] += 1
        
        elif 2400 <= A <= 2799:
            rate["dai"] += 1
        
        elif 2800 <= A <= 3199:
            rate["aka"] += 1
        
        else:
            rate["free"] += 1
    
    rate_len_nofree = len(rate)-1 if "free" in rate else len(rate)
    ans_min = rate_len_nofree
    ans_max = rate_len_nofree + rate["free"]

    if len(rate) == 1 and "free" in rate:
        ans_min = 1

    print(ans_min, ans_max)

if __name__ == '__main__':
    sys.exit(main())
