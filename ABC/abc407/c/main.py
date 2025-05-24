import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    s = input()
    ans = float("inf")
    
    for num in range(10):
        anst = 0
        for c in s:
            dist = ord(c)-ord('0')
            bcnt = (num-dist)%10
            mod = anst % 10
            if mod <= bcnt:
                anst += bcnt-mod
            else:
                anst += 10-(mod-bcnt)
        
        
        anst += (num-anst)%10
        ans = min(ans, anst)
    
    print(ans+len(s))


if __name__ == '__main__':
    sys.exit(main())
