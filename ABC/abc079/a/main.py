import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = input()
    
    print("Yes" if n[0]==n[1]==n[2] or n[1]==n[2]==n[3] else "No")
    
    


if __name__ == '__main__':
    sys.exit(main())
