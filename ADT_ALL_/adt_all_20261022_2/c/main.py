def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    st = []
    for _ in range(n):
        st.append(input()[:-1])

    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if st[i] == st[j]:
               print("Yes")
               return
    print("No")

if __name__ == "__main__":
    main()
