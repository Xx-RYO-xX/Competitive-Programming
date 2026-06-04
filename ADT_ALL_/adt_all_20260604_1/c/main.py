import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    st = []
    for _ in range(n):
        s, t = input().split()
        st.append((s, t))

    for i in range(n):
        s, t = st[i]
        c1 = False
        c2 = False
        for j in range(n):
            s1, t1 = st[j]
            if i == j:
                continue
            if s == s1 or s == t1:
                c1 = True
            if t == t1 or t == s1:
                c2 = True
        if c1 and c2:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
