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
    a = int(input())
    n = int(input())
    
    ans = 0
    
    pad_ten = []
    
    for i in range(1, 10):
        if i <= n:
            pad_ten.append(i)
    
    len_max = len(str(n))
    
    for keta in range(2, len_max+1):
        if keta % 2 == 0:
            half_keta = keta // 2
            start = 10**(half_keta-1)
            end = 10**half_keta
            
            for i in range(start, end):
                s = str(i)
                pad_str = s+s[::-1]
                if int(pad_str) > n:
                    break
                pad_ten.append(int(pad_str))
        
        else:
            half_keta = keta//2
            start = 10**half_keta
            end = 10**(half_keta+1)
            
            for i in range(start, end):
                s = str(i)
                pad_str = s+s[-2::-1]
                if int(pad_str) > n:
                    break
                pad_ten.append(int(pad_str))

    
    for num in pad_ten:
        num_a = base_n(num, a)
        if str(num_a) == str(num_a)[::-1]:
            ans += num
    
    print(ans)


if __name__ == '__main__':
    main()
