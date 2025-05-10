import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    
    n = int(input())
    y_to_xi = defaultdict(list)
    yy = set()
    for i in range(n):
        x, y = map(int, input().split())
        y_to_xi[y].append((x, i))
        yy.add(y)
    s = input()
    
    for y in yy:
        if len(y_to_xi[y]) >= 2:
            y_to_xi[y].sort()
            right_cond = False
            for x, i in y_to_xi[y]:
                if s[i] == "R":
                    right_cond = True
                if right_cond and s[i] == "L":
                    print("Yes")
                    return
    
    print("No")
    


if __name__ == '__main__':
    sys.exit(main())
