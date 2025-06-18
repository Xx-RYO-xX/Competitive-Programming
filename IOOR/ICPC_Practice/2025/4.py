import sys


def input():return sys.stdin.readline().rstrip()


def main():
    while True:
        a, l = map(int, input().split())
        if a==l==0: return
        a_lst = set([a])
        value_i = {a:0}
        a = list(str(a).zfill(l))
        # print(a, a_lst)
        
        j = 1
        while True:
            max_value = int("".join(sorted(a, reverse=True)))
            min_value = int("".join(sorted(a)))
            # print(max_value, min_value)
            anst = max_value-min_value
            if anst in a_lst:
                print(value_i[anst], anst, j-value_i[anst])
                break
            
            a = list(str(anst).zfill(l))
            a_lst.add(anst)
            value_i[anst] = j
            j += 1

if __name__ == '__main__':
    main()
