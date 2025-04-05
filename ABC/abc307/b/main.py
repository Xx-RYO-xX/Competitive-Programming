import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n =int(input())
    s = []
    for _ in range(n):
        s.append(input())
    
    for i in range(n):
        for j in range(n):
            if i != j:
                string = s[i]+s[j]
                if string == string[::-1]:
                    print("Yes")
                    return
    print("No")
    

if __name__ == '__main__':
    main()
