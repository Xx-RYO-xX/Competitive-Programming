import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    MOD = 998244353

    q = int(input())
    s = 1
    s_str = [1]
    slen = 1
    sentou_idx = 0
    for _ in range(q):
        query = input()
        if query[0] == "1":
            Q, x = map(int, query.split())
            s *= 10
            s += x
            s %= MOD
            s_str.append(x)
            slen += 1
        if query[0] == "2":
            sentou = s_str[sentou_idx]
            sentou_idx += 1
            slen -= 1
            minus = (sentou * pow(10, slen, MOD)) % MOD
            # print(sentou, minus)
            s -= minus
            s %= MOD

        if query[0] == "3":
            # print(s_str)
            print(s % MOD)


if __name__ == "__main__":
    main()
