import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, h, d = map(int, input().split())
    hd = []
    for _ in range(n):
        h, d = map(int, input().split())
        hd.append((h, d))
    
    

if __name__ == '__main__':
    main()
