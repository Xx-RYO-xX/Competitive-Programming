import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    
    ans = []
    
    for i in range(1, 10):
        for j in range(1, 10):
            s_u_m = 0
            for k in range(1, 10):
                for l in range(1, 10):
                    if (i, j) != (k, l):
                        s_u_m += k*l
            if s_u_m == n:
                ans.append(str(i)+" x "+str(j))
    
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
