import sys

def input():return sys.stdin.readline().rstrip()


def main():
    from atcoder.lazysegtree import LazySegTree
    n = int(input())
    a = list(map(int, input().split()))
    
    def op(num1, num2):
        return num1 + num2

    def mapping(lazy_upper, data_lower):
        return lazy_upper + data_lower
    
    def composition(lazy_upper, lazy_lower):
        return lazy_upper + lazy_lower
    
    naguru = LazySegTree(op=op, e=0, mapping=mapping, composition=composition, id_=0, v=a)
    
    # print(naguru)
    for i in range(n):
        isi = naguru.get(i)
        kubaru_idx =  min(n, i+isi+1)
        naguru.apply(i+1, kubaru_idx, 1)
        naguru.set(i, isi-(kubaru_idx-i)+1)
    
    for i in range(n):
        print(naguru.get(i), end=" ")
        


if __name__ == '__main__':
    sys.exit(main())
