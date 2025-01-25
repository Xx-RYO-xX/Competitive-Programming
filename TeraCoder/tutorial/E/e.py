"""実装例"""

T = int(input())
for i in range(1, T+1):
    print('Case #', i, ':', sep='')
    N = int(input())
    print((N * (N+1))//2)
