import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n,m = map(int, input().split())
    b = list(map(int, input().split()))
    for i in range(m-1):
        if b[i+1]-b[i] != 1:
            print("No")
            return
    if (b[0]-1)%7+m > 7:
        print("No")
        return
    
    for _ in range(n-1):
        nb = list(map(int, input().split()))
        for i in range(m):
            if i != m-1 and nb[i+1]-nb[i] != 1:
                print("No")
                return
            if nb[i]-b[i]!= 7:
                # print(nb[i], b[i])
                print("No")
                return
        b = nb
    
    print("Yes")
    
    
    # for i in range(1, 11):
    #     for j in range(1, 8):
    #         print((i-1)*7+j, end=" ")
    #     print()
    


if __name__ == '__main__':
    main()
