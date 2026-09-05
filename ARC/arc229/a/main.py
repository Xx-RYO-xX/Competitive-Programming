def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    
    if x == 0:
        print("A")
        return
    al = x //25
    ar = x % 25
    ans = "a"*al

    ans += "c"*25
    ans = list(ans)
    if ar != 0:ans.insert(-ar, "a")
    print(ans[0].upper(), end="")
    for i in range(1, len(ans)):
        print("R"+ans[i].upper(), end="")


if __name__ == "__main__":
    main()
