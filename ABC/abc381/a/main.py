import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = list(input())
    
    if n % 2 == 0 and n != 1:
        print('No')
        return
    mid = n // 2
    for i in range(mid):
        if s[i] != "1":
            print("No")
            return
    if s[mid] != "/":
        print("No")
        return
    for i in range(mid+1, n):
        if s[i] != "2":
            print("No")
            return
    
    print("Yes")
    

if __name__ == '__main__':
    main()
