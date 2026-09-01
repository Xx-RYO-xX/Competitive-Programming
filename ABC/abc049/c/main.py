def main():
    import sys

    input = sys.stdin.readline
    
    s = list(input())[:-1]

    moji = [list("dream"), list("dreamer"), list("erase"), list("eraser")]
    while s:
        cond =True 
        for i in [5, 6, 7]:
            if len(s) >= i and s[-i:] in moji:
                for _ in range(i):
                    s.pop()
                cond =False 
        if cond:
            break
    print("YES" if not s else "NO")
if __name__ == "__main__":
    main()
