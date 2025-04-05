import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = input()
    
    ans = []
    for i in range(2 ** len(n)):
        s_u_m = ""
        for j in range(len(n)):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += n[j]
        if s_u_m != "" and int(s_u_m) % 3 == 0:
            ans.append(s_u_m)

    # print(ans)
    try:
        print(len(n)-len(max(ans, key=len)))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
