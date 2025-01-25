import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations
    h, w, d = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    
    floor = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                floor.append((i, j))
    
    max_count = 0
    for (x1, y1), (x2, y2) in combinations(floor, 2):
        humid = set()
        for x, y in floor:
            if abs(x-x1) + abs(y-y1) <= d or abs(x-x2) + abs(y-y2) <= d:
                humid.add((x, y))
        count = len(humid)
        if count > max_count:
            max_count = count
    
    print(max_count)

if __name__ == '__main__':
    main()
