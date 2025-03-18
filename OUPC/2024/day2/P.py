import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    n = int(input())
    a = list(input().split())
    b = list(map(int, input().split()))
    
    ans_dict = defaultdict(int)
    for i in range(n):
        ans_dict[a[i]] += b[i]

    ans_dict["i"] %= 4
    ans_dict['-i'] %= 4
    
    if ans_dict["i"] == 0: ans_dict.pop("i")
    if ans_dict["-i"] == 0: ans_dict.pop("-i")
    
    # print(ans_dict)
    ans = 1
    for num in ans_dict:
        numt = 0
        if num == "i":
            numt = 1j
        elif num == "-i":
            numt = -1j
        else:
            numt = int(num)
        ans *= numt**ans_dict[num]
    
    if int(ans.real) == 1 or int(ans.real) == -1:
        print(int(ans.real))
    else:
        if str(ans.imag)[0] == "1":
            print("i")
        else:
            print("-i")


if __name__ == '__main__':
    main()
