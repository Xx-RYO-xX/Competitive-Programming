def main():
    import sys

    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        a = sorted(map(int,input().split()))
        gk = [[], [], []]
        for i in range(n-2):
            if a[i]%2==0:
                gk[1].append(a[i])
            else:
                gk[2].append(a[i])
        
        ansl = [a[-1]]
        guuki = -1 if a[-1] % 2 == 0 else 1
        for i in range(n-2):
            poped = gk[guuki].pop() if gk[guuki] else gk[-guuki].pop()
            ansl.append(poped)
            guuki *= -1
        ans = 0
        for i in range(n-2):
            ans += (ansl[i] + ansl[i+1]) // 2
        print(ans+(ansl[i]+a[-2])//2)

if __name__ == "__main__":
    main()

