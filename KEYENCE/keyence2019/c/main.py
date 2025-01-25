import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ab = [aa-bb for aa, bb in zip(a, b)]
    
    # print(ab)
    if sum(ab) < 0:
        print(-1)
        return
    
    plus = []
    minus = []
    for AB in ab:
        if  0 <= AB:
            plus.append(AB)
        else:
            minus.append(AB)
    
    if len(minus) == 0:
        print(0)
        return

    plus.sort(reverse=True)
    
    idx = 0
    for MINUS in minus:
        plus[idx] += MINUS
        if plus[idx] <= 0:
            plus[idx+1] += abs(plus[idx])
            idx += 1
    
    print(2*(idx+1)+1)

if __name__ == '__main__':
    main()
