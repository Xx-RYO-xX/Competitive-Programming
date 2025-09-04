import sys


def input():
    return sys.stdin.readline().rstrip()


def base_n(number, base):
    """
    10進数をn進数に変換する関数だっピ\n
    ￣￣V￣￣￣￣￣￣￣￣￣￣￣￣￣￣\n
    ( ・3・)\n
    /｜｜｜\\
    
    Parameters
    ----------
    number : int
        10進数の数値
    base : int
        変換したいn進数
        
    Returns
    -------
    return : str
        n進数に変換された文字列
    """
    if number < 0:
        return "-" + base_n(-number, base)
    elif number < base:
        return str(number)
    else:
        return base_n(number // base, base) + str(number % base)


def main():
    k = int(input())

    print(base_n(k, 2).replace("1", "2"))


if __name__ == "__main__":
    main()
