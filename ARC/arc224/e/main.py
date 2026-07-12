def main():
    import sys

    input = sys.stdin.readline

    for _ in range(int(input())):
        s = list(input().rstrip())

        stack = []
        a_idx = []
        ans = 0
        for S in s:
            match S:
                case "A":
                    stack.append(S)
                    a_idx.append(len(stack) - 1)
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
                            a_idx.pop()
                        else:
                            break
                    else:
                        stack.clear()
                        a_idx.clear()
                        ans += 1

        print(ans)


if __name__ == "__main__":
    main()
