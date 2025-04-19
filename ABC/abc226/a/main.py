import sys 
import decimal


def input():return sys.stdin.readline().rstrip()


def rounding(num, digit):
    """
    四捨五入を正確にする関数

    Parameters
    ----------
    num : float or int or str
        四捨五入したい数
    digit : int
        丸める桁数

    Returns
    -------
    return : decimal.Decimal
        四捨五入された数値

    Notes
    -----
    - digitが2以上の場合(2桁目以降に丸める時)、指数表記になるのでキャストが必要
    """
    deci = 10 ** digit if digit != 0 else 0
    return (decimal.Decimal(str(num)).
            quantize(decimal.Decimal(str(deci) if deci < 1 else "1E" + str(digit - 1)), decimal.ROUND_HALF_UP))


def main():
    n = float(input())
    print(rounding(n, 1))
    
    


if __name__ == '__main__':
    sys.exit(main())
