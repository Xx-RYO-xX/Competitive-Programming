def main():
    import sys

    input = sys.stdin.readline
    ss = input()[:-1]
    tt = input()[:-1]
    pen = "ABCDEABCDE"

    def kyori(s1, s2):
        ans = []
        s1_idx = [i for i, x in enumerate(pen)if x == s1]
        s2_idx = [i for i, x in enumerate(pen)if x == s2]

        for i in range(2):
            for j in range(2):
                ans.append(abs(s1_idx[i]-s2_idx[j]))
        return min(ans)
    print("Yes" if kyori(ss[0], ss[1])==kyori(tt[0], tt[1]) else "No")
if __name__ == "__main__":
    main()
