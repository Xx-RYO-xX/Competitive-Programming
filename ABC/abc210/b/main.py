import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    
    for i in range(n):
        if s[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            exit()


if __name__ == '__main__':
    main()
