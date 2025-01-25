import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(n):
        if s[i] == "/":
            left = i-1
            right = i+1 
            count = 0
            while 0<=left and right<n:
                if s[left] == "1" and s[right] == "2":
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            ans = max(ans, count)
    print(ans*2+1)
if __name__ == '__main__':
    main()
