def main():
    t = int(input())
    for T in range(1, t+1):
        print("Case #%d:" % T)
        
        n = int(input())
        if 2013 <= n <= 2022:
            print(n-2013)
        elif n == 2024:
            print(11)

if __name__ == '__main__':
    main()