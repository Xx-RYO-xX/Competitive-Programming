def main():
    t = int(input())
    for T in range(1, t+1):
        print("Case #%d:" % T)
        n = int(input())
        p = list(map(int, input().split()))
        m = int(input())
        s = list(map(int, input().split()))
        o = int(input())
        l = list(map(int, input().split()))

        s_sum = 0
        l_sum = 0
        for i in range(m):
            s_sum += p[s[i]-1]
        
        for i in range(o):
            l_sum += p[l[i]-1]

        print(s_sum, l_sum, s_sum + l_sum)

if __name__ == '__main__':
    main()