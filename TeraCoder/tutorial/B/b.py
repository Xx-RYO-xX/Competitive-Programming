"""実装例"""

T = int(input())
for i in range(1, T+1):
    print('Case #', i, ':', sep='')

    a, b = map(int, input().split())
    quotient = a // b
    remainder = a % b

    print(quotient, remainder)
