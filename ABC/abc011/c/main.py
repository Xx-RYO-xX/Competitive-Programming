import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    ng = set()
    for _ in range(3):
        ng.add(int(input()))
    if n in ng:
        print("NO")
        return 
    for _ in range(100):
        n -= 3
        for i in range(1, 4)[::-1]:
            if n in ng:
                n += i
                n -= i-1

        if n in ng:
            print("NO")
            return 
        
        
        if n <= 0:
            print("YES")
            return
    print("NO")
    




if __name__ == '__main__':
    sys.exit(main())
