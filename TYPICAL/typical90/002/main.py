import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import combinations
    n = int(input())
    if n % 2 != 0:
        exit()
    
    lst = sorted([bin(i)[2:].zfill(n) for i in range(2**n)])
    # print(lst)
    for LST in lst:
        score = 0
        for s in LST:
            if s == "0":
                score += 1
            else:
                score -= 1
            if score < 0:
                break
        else:
            if score == 0:
                print("".join(["(" if i == "0" else ")" for i in LST]))


if __name__ == '__main__':
    sys.exit(main())
