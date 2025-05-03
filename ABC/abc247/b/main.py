import sys


def input(): return sys.stdin.readline().rstrip()


def main():

    n = int(input())
    s, t = [], []
    for _ in range(n):
        st, tt = input().split()
        s.append(st)
        t.append(tt)

    for i in range(n):
        can_use_name1 = True
        can_use_name2 = True
        
        for j in range(n):
            if i == j:  
                continue
            
            if s[i] == s[j] or s[i] == t[j]:
                can_use_name1 = False
            
            if t[i] == s[j] or t[i] == t[j]:
                can_use_name2 = False
        
        if not can_use_name1 and not can_use_name2:
            print("No")
            return
    
    print("Yes")



if __name__ == '__main__':
    sys.exit(main())
