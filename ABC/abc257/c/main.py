import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import Counter
    n = int(input())
    s = list(input())
    w = list(map(int, input().split()))
    
    w_s = sorted((ww, ss) for ww, ss in zip(w, s))

    correct = Counter(s)
    robot = {"0":0, "1":correct["1"]}
    ans =  max(correct["0"], correct["1"])
    for i in range(n):
        ww, ss = w_s[i]
        if ss == "0":
            robot["0"] += 1
        else:
            robot["1"] -= 1
        if ww != w_s[(i+1)%n][0]:
            ans = max(ans, robot["0"]+robot["1"])
    
    print(ans)

if __name__ == '__main__':
    main()
