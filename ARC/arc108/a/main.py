import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s, p = map(int, input().split())
    
    for m in range(10**7):
        if (s-m)*m == p:
            print("Yes")
            exit()

    print("No")



if __name__ == '__main__':
    main()
