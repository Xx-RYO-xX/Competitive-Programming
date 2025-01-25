"""実装例"""

T = int(input())
for i in range(1, T+1):
    print('Case #', i, ':', sep='')
    n = int(input())
    a = list(map(int, input().split()))

    total_sum = sum(a)

    print(total_sum)
