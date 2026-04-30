import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(2**n):
        if i % 2 != 0:
            continue
        s_u_m = ""
        for j in range(n):
            bit = 2**j
            if (i // bit) % 2 == 1:
                s_u_m += "+"
            s_u_m += s[j]
        ans += eval(s_u_m)

    print(ans)


if __name__ == "__main__":
    main()
