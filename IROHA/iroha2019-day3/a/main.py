import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from itertools import permutations
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = map(int, input().split())

    print(A-B)
    print(C+D)
    print(F-E if F-E >= 0 else 0)
    print((G+H+I)//3 + 1)
    print("".join(list(permutations("dagabaji", J))[0]))
    

if __name__ == '__main__':
    sys.exit(main())
