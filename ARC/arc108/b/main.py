import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()
    
    stuck = []
    
    for i in range(n):
        stuck.append(s[i])
        if len(stuck) >= 3 and "".join(stuck[-3:]) == "fox":
            for i in range(3):
                stuck.pop()
    
    print(len(stuck))


if __name__ == '__main__':
    main()
