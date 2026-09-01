def main():
    import sys

    input = sys.stdin.readline
    c = input()[:-1]

    if c in "aeiou":
        print("vowel")
    else:
        print("consonant")

if __name__ == "__main__":
    main()
