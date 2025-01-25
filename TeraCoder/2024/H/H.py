def main():
    # import time
    # start = time.time()
    MOD = 998244353
    t = int(input())
    for T in range(1, t+1):
        print("Case #%d:" % T)
        a, n = map(int, input().split())
        n_sum = ((n*(n+1))//2)**2
        a_sum = ((a*(a-1))//2)**2
        print((n_sum-a_sum)%MOD)
        # ans = 0
        # for i in range(a, n+1):
        #     ans += i**3
    #     # print(ans%MOD)
    # end = time.time()
    # print("Time:", end-start)

if __name__ == '__main__':
    main()