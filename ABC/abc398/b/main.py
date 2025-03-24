import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    a = Counter(list(map(int, input().split())))
    
    cond3 = [k for k, v in a.items() if v >= 3]  
    cond2 = [k for k, v in a.items() if v >= 2]  
    
    print("Yes" if cond3 and len(cond2) >= 2 else "No")
    
    

if __name__ == '__main__':
    sys.exit(main())
