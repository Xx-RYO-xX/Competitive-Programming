import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    a, b, c, d = map(int, input().split())
    mod = 998244353
    
    # オレンジとバナナを組み合わせる方法
    result = combination_mod(b + c, b, mod)
    print(result)


def factorial_mod(n, mod):
    """mod を法とする階乗を計算"""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result


def pow_mod(x, n, mod):
    """mod を法とするxのn乗を計算"""
    result = 1
    while n > 0:
        if n & 1:
            result = (result * x) % mod
        x = (x * x) % mod
        n >>= 1
    return result


def inverse_mod(x, mod):
    """mod を法とするxの逆元を計算"""
    return pow_mod(x, mod - 2, mod)


def combination_mod(n, r, mod):
    """mod を法とする組み合わせ nCr を計算"""
    if r < 0 or r > n:
        return 0
    num = factorial_mod(n, mod)
    den = (factorial_mod(r, mod) * factorial_mod(n - r, mod)) % mod
    return (num * inverse_mod(den, mod)) % mod


if __name__ == '__main__':
    sys.exit(main())
