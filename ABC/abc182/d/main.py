import sys


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    robot = 0
    move = 0
    move_max = 0
    for i in range(n):
        move = move + a[i]
        move_max = max(move_max, move)
        ans = max(robot+move_max, ans)
        robot += move
        # print(ans, move_max)
    
    print(ans)

if __name__ == '__main__':
    main()
