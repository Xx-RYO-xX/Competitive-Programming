import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    s = input()
    sonzai = set()
    if len(s) % 2 != 0:
        print("No")
        exit()
    for i in range(len(s)//2):
        # print(i)
        if s[2*i] == s[2*i+1] and s[2*i] not in sonzai:
            sonzai.add(s[2*i])
        else:
            print("No")
            exit()
    
    print("Yes")
    

if __name__ == '__main__':
    main()
