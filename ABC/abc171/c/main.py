import sys 


def input():return sys.stdin.readline().rstrip()


def base_n(number, base):
    """
    10進数をn進数に変換する関数
    
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
        return '-' + base_n(-number, base)
    elif number < base:
        return str(number)
    else:
        return base_n(number // base, base) + str(number % base)



def main():
    n = int(input())
    ans = base_n(n, 26)
    name = ''.join([chr(97 + int(c)) for c in ans])
    print(name)


if __name__ == '__main__':
    sys.exit(main())
