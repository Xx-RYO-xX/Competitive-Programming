import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    
    ans = [1]
    for i in range(2, n+1):
        if i - ans[-1] != 1:
            ans.append(i)

    # print(ans)
    if k <= len(ans):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    sys.exit(main())
