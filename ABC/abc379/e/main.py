import sys
# from functools import cache

# sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

# @cache
def calc_f(s, i, now_f):
    if i >= len(s):
        return 0
    num = int(s[i])
    new_f = now_f * 10 + num * (i + 1)
    return new_f + calc_f(s, i + 1, new_f)


def main():
    sys.set_int_max_str_digits(0)
    sys.set_int_max_str_digits(0)
    n = int(input())
    s = input()
    ans = calc_f(s, 0, 0)
    print(ans)

if __name__ == "__main__":
    main()
