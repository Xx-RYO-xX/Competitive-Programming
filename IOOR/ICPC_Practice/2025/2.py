import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        n, p = map(int, input().split())
        if n == p == 0: return
        
        sums = p
        wan = p
        hand = [0]*n
        idx = 0
        
        while True:
            if wan > 0:
                wan -= 1
                hand[idx] += 1
                if wan == 0 and hand[idx] == sums:
                    print(idx)
                    break
            else:
                if hand[idx] > 0:
                    wan = hand[idx]
                    hand[idx] = 0
            idx = (idx+1)%n
        

if __name__ == '__main__':
    main()
