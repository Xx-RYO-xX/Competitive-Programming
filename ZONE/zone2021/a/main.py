import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    
    ans = s.count("ZONe")

    print(ans)

if __name__ == '__main__':
    main()
