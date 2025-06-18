import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    count_C = 0
    count_D = 0 
    for c in s:
        if c == "(":
            count_C += 1
        else:
            count_D += 1
    
    print(count_C, count_D)
    
    len_s = len(s)
    if count_C < count_D:
        inserted_count = 0
        for i in range(len_s):
            if s[i+inserted_count] 

if __name__ == '__main__':
    sys.exit(main())
