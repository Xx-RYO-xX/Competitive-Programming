import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    s = input()

    MOD = 998244353

    ans = 0
    moji = {"C", "P", "U", "K"}
    basho = {"C": 0, "P": 0, "U": 0, "K": 0}
    lens = {
        "P": 1,
        "U": 2,
        "K": 3,
    }

    stack = []
    for i in range(n)[::-1]:
        if s[i] in moji:
            if s[i] == "C":
                stack.append([i + 1])
                basho[s[i]] += 1
            else:
                if len(stack) > basho[s[i]] and len(stack[basho[s[i]]]) == lens[s[i]]:
                    stack[basho[s[i]]].append(i + 1)
                    basho[s[i]] += 1

                    if stack and s[i] == "K" and len(stack[basho[s[i]] - 1]) == 4:
                        # print(stack[basho[s[i]] - 1])
                        anst = 1
                        for nums in stack[basho[s[i]] - 1]:
                            anst *= nums
                            anst %= MOD
                        ans += anst
                        ans %= MOD
        # print(stack, basho)
    print(ans % MOD)


if __name__ == "__main__":
    main()
