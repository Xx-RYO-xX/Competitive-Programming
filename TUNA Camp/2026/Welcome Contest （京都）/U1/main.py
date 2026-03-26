s = list(input())
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(s)):
    for c in list(AZ):
        ss = s.copy()
        ss[i] = c
        if ss == ss[::-1]:
            print("Yes")
            exit()

print("No")
