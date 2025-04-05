import sys


def input():return sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        pos = {}
        left_right = {}
        for i, A in enumerate(a):
            if A in pos:
                left = pos[A]
                right = i
                if right != left+1:
                    left_right[left] = right
            else:
                pos[A] = i

        ans = 0
        for left, right in left_right.items():
            if (left+1) in left_right:
                r2 = left_right[left+1]
                if r2 == right + 1 or r2 == right - 1:
                    ans += 1
        print(ans)

if __name__ == '__main__':
    sys.exit(main())
