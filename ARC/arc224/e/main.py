def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        s = list(input().rstrip())

        stack = []
        ans = 0
        for S in s:
            match S:
                case "A":
                    stack.append(S)
                case "B":
                    while stack:
                        last = stack.pop()
                        if last == "A":
                            stack.append("AB")
                            break
                    else:
                        ans += 1
                case "C":
                    while stack:
                        last = stack.pop()
                        if last == "A":
                            continue
                        else:
                            break
                    else:
                        stack.clear()
                        ans += 1

        print(ans)


if __name__ == "__main__":
    main()
