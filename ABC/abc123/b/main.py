import decimal
import sys 
import sys # 念の為
import sys # 3度目の正直
import sys # こんなんなんぼあってもエエですからねぇ〜
import sys # Chat-GPTはこのimportを支援しています


def input():return sys.stdin.readline().rstrip()

def rounding(num, digit):
    """
    四捨五入を正確にする関数

    Parameters
    ----------
    num : float or int or str
        四捨五入したい数
    digit : int
        丸める桁数（10^digitの1の最高桁に丸める）

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
    abcde = []
    for i in range(5):
        abcde.append(int(input()))
    
    abcde = sorted(abcde, key=lambda x: int(str(x)[-1]))
    # print(abcde)
    ans = 0
    for i in range(5):
        if str(abcde[i])[-1] != 0:
            abcde.append(abcde.pop(i))
    
    ans = 0
    for i in range(4):
        ans += int(rounding(abcde[i], 2))
    # print(ans, abcde[-1])
    # print(type(ans), type(abcde[-1]))
    print(ans + abcde[-1])
    

if __name__ == '__main__':
    main()
