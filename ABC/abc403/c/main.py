import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n, m, q = map(int, input().split())
    kengen = defaultdict(set)
    for _ in range(q):
        query = input()
        
        if query[0] == "1":
            qq, x, y = map(int, query.split())
            kengen[x].add(y)
            
        elif query[0] == "2":
            qq, x = map(int, query.split())
            kengen[x].add("all")
        
        else:
            qq, x, y = map(int, query.split())
            if y  in kengen[x] or "all" in kengen[x]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    sys.exit(main())
