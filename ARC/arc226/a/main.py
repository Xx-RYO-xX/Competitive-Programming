def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    kaburi = [0] * (2 * n + 2)
    st = []
    for _ in range(n):
        s, t = map(int, input().split())
        st.append([s, t])
        kaburi[s] += 1
        kaburi[t + 1] -= 1

    # print(kaburi)
    for i in range(1, 2 * n + 1):
        kaburi[i] += kaburi[i - 1]
        if kaburi[i] > 2:
            print(0)
            return
    st.sort()

    kukan = [st[0][:]]
    for ss, tt in st[1:]:
        s, t = kukan[-1]
        if s <= ss <= t:
            if tt <= t:
                pass
            else:
                kukan[-1][1] = tt
        else:
            kukan.append([ss, tt])
    # print(kukan)

    print(pow(2, len(kukan), 998244353))


if __name__ == "__main__":
    main()
