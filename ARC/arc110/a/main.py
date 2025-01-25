import sys 


def input():return sys.stdin.readline().rstrip()



def main():
    import math
    n = int(input())
    print(math.lcm(*range(2, n+1))+1)

if __name__ == '__main__':
    main()
