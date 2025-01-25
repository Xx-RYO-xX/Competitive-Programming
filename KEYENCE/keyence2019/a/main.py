import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    n_lst = list(input().split())

    for LST in list(permutations(n_lst, 4)):
        # print(LST)
        if "".join(LST) == "1974":
            print("YES")
            return
    
    print("NO")


if __name__ == '__main__':
    sys.exit(main())