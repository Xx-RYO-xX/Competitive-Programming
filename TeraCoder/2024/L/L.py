def is_palindrome(s):
    return s == s[::-1]


def main():
    t = int(input())
    for T in range(1, t+1):
        print("Case #%d:" % T)
        
        n = int(input())
        s = []
        for _ in range(n):
            s.append(input())
        
        
        terako = 2 if is_palindrome(s[0]) else 1
        terako_a = 0
        is_say = set()
        for i in range(1, n):
            if s[i][0] == s[i-1][-1] and s[i] not in is_say:
                if i % 2 == 0:
                    terako += 2 if is_palindrome(s[i]) else 1
                else:
                    terako_a += 2 if is_palindrome(s[i]) else 1
                is_say.add(s[i])
            else:
                break
        
        if terako > terako_a:
            print("Terako")
            print(terako)
        elif terako < terako_a:
            print("TerakoA")
            print(terako_a)
        else:
            print("draw")
            print(-1)


if __name__ == '__main__':
    main()
