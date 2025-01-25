import sys 


def input(): return sys.stdin.readline().rstrip()


def main():
    n, x = map(int, input().split())
    v = []
    a = []
    c = []
    
    max_vit = 0
    for _ in range(n):
        vt, at, ct = map(int, input().split())
        v.append(vt)
        a.append(at)
        c.append(ct)
        max_vit = max(max_vit, at)
    
    def check(target):
        items = [[] for _ in range(4)]
        for i in range(n):
            items[v[i]].append((c[i], a[i], i))
        for i in range(4):
            items[i].sort(key=lambda x: x[0])  
        
        used_calorie = 0
        used = set()
        
        for vit in range(1, 4):
            current = 0
            for cal, amt, idx in items[vit]:
                if current >= target:
                    break
                if idx not in used and used_calorie + cal <= x:
                    current += amt
                    used_calorie += cal
                    used.add(idx)
                    
            if current < target:
                return False
                
        return True
    
    left = 0
    right = max_vit + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    
    print(left)

if __name__ == "__main__":
    main()
